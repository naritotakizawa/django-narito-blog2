# django-narito-blog2
シンプルすぎるブログ

## 動作環境
Django2.2以上

## 使い方
インストールする。

```python
pip install https://github.com/naritotakizawa/django-narito-blog2/archive/master.tar.gz
```

`settings.py`に追加する。

```python
INSTALLED_APPS = [
    'nblog2.apps.Nblog2Config',  # これ
    'django.contrib.humanize',  # これ
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

```python
# アップロードファイルの設定
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

```python
# マークダウンの拡張
MARKDOWN_EXTENSIONS = [
    'markdown.extensions.extra',
    'markdown.extensions.toc',
]
```

`urls.py`に追加する。

```python
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('nblog2.urls')),
]


# 開発環境でのメディアファイルの配信設定
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
```


マイグレートやスーパーユーザーを作成する。

```
python manage.py migrate
python manage.py createsuperuser
```

`nblog2/base_site.html`を上書きすることで、ブログ内のタイトル等の情報を上書きできます。例えば、次のように上書きします。

```html
{% extends 'nblog2/base.html' %}

{% block extrahead %}
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-72333380-3"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() {
            dataLayer.push(arguments);
        }
        gtag('js', new Date());
        gtag('config', 'UA-72333380-3');
    </script>

    <!-- Google Ads -->
    <script data-ad-client="ca-pub-5235456993770661" async
            src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
{% endblock %}

{% block meta_title %}DESIGN NOTE{% endblock %}
{% block meta_description %}デザインに関する、自分用のノートです。{% endblock %}

{% block title %}DESIGN NOTE{% endblock %}

{% block copyright %}© 2019 Narito Takizawa{% endblock %}

{% block link %}
    <li><a href="https://twitter.com/toritoritorina/" target="_blank">Twitter</a></li>
    <li><a href="https://github.com/naritotakizawa/" target="_blank">Github</a></li>
    <li><a href="https://narito.ninja/" target="_blank">プログラミング関連のブログ</a></li>
    <li><a href="https://narito.ninja/diaries/" target="_blank">日記</a></li>
    <li><a href="mailto:toritoritorina@gmail.com" target="_blank">メール</a></li>
    <li><a href="https://github.com/naritotakizawa/django-narito-blog2/" target="_blank">ソースコード</a></li>
{% endblock %}
```
