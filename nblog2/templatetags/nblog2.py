from urllib import parse
from django import template
from django.conf import settings
from django.shortcuts import resolve_url
from django.utils.safestring import mark_safe
import markdown
from markdown.extensions import Extension

register = template.Library()


@register.simple_tag
def url_replace(request, field, value):
    """GETパラメータの一部を置き換える。"""
    url_dict = request.GET.copy()
    url_dict[field] = str(value)
    return url_dict.urlencode()


@register.filter
def markdown_to_html(text):
    """マークダウンをhtmlに変換する。"""
    html = markdown.markdown(text, extensions=settings.MARKDOWN_EXTENSIONS)
    return mark_safe(html)


@register.simple_tag
def get_return_link(request):
    top_page = resolve_url('nblog2:note_list')
    referer = request.environ.get('HTTP_REFERER')
    # URL直接入力やお気に入りアクセスのときはリファラがないので、トップぺージに戻す
    if referer:
        # リファラがある場合、前回ページが自分のサイト内であれば、そこに戻す。
        parse_result = parse.urlparse(referer)
        if request.get_host() == parse_result.netloc:
            return referer
    return top_page
