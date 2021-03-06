from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


LOCAL_MCE_FILEBROWSER_JQUERY = getattr(settings, 'MCE_FILEBROWSER_JQUERY', None)
LOCAL_MCE_FILEBROWSER_UPLOADDIR = getattr(settings, 'MCE_FILEBROWSER_UPLOADDIR', 'mce_filebrowser')
LOCAL_MCE_FILEBROWSER_THEMECSS = getattr(settings, 'MCE_FILEBROWSER_THEMECSS', None)
LOCAL_MCE_FILEBROWSER_PERUSER = getattr(settings, 'MCE_FILEBROWSER_PERUSER', True)

LOCAL_MCE_FILEBROWSER_DECORATOR_MODULE = getattr(settings, 'MCE_FILEBROWSER_DECORATOR_MODULE', 'django.contrib.admin.views.decorators')
LOCAL_MCE_FILEBROWSER_DECORATOR_METHOD = getattr(settings, 'MCE_FILEBROWSER_DECORATOR_METHOD', 'staff_member_required')


if LOCAL_MCE_FILEBROWSER_JQUERY == None:
    raise ImproperlyConfigured("MCE_FILEBROWSER_JQUERY must be set (path relative to your static files root)")

if LOCAL_MCE_FILEBROWSER_THEMECSS == None:
    raise ImproperlyConfigured("MCE_FILEBROWSER_THEMECSS must be set (path relative to your static files root). This should be the path to the TinyMCE theme css file.")