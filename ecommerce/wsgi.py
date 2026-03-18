"""
WSGI config for ecommerce project.
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecommerce.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

# Auto-migrate and seed on Vercel cold start
if os.environ.get('VERCEL'):
    try:
        from django.core.management import call_command
        call_command('migrate', '--run-syncdb', verbosity=0)
        from store.models import Product
        if Product.objects.count() == 0:
            call_command('seed_products', verbosity=0)
    except Exception:
        pass

app = application
