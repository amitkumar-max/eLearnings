import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')  # 'config' ko aapke project folder name se replace karo

application = get_wsgi_application()
