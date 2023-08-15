
from django.utils.html import format_html
from django.templatetags.static import static

from wagtail import hooks

@hooks.register('insert_global_admin_css')
def global_admin_css():
    return format_html('<link rel="stylesheet" href="{}">', static('css/theme-color/theme-yale-blue.css'))


        # <link rel="stylesheet" type="text/css" href="{% static 'css/bootstrap.min.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/animate.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/fontawesome-all.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/themify-icons.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/audioplayer/media-player.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/magnific-popup/magnific-popup.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/owl-carousel/owl.carousel.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/base.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/shortcodes.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/responsive.css' %}">
        # <link rel="stylesheet" type="text/css" href="{% static 'css/theme-color/theme-yale-blue.css' %}">