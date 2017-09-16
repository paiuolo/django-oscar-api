import os


location = lambda x: os.path.join(
    os.path.dirname(os.path.realpath(__file__)), x)

MEDIA_ROOT = location('../static')
STATIC_URL = '/static/'

MEDIA_ROOT = location('../media')
MEDIA_URL = '/media/'