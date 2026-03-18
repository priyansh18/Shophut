"""
WSGI config for ecommerce project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

application = get_wsgi_application()

# Auto-migrate and seed on Vercel (serverless cold start)
if os.environ.get('VERCEL'):
    from django.core.management import call_command
    import django
    django.setup()
    call_command('migrate', '--run-syncdb', verbosity=0)
    from store.models import Product
    if Product.objects.count() == 0:
        call_command('seed_products', verbosity=0)

app = application
