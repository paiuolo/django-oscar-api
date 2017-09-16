EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.example.org'
EMAIL_HOST_USER = 'info@example.org'
EMAIL_HOST_PASSWORD = 'password'

EMAIL_USE_TLS = True
EMAIL_PORT = 587