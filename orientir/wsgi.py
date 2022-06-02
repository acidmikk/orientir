"""
WSGI config for rapir_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

#import os

#from django.core.wsgi import get_wsgi_application

#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rapir_site.settings')

#application = get_wsgi_application()

# -*- coding: utf-8 -*-
import os
import sys
import config
import platform
#путь​ к проекту, там где manage.py
sys.path.insert(0, config.project_path + 'orientir')
#путь​ к фреймворку, там где settings.py
sys.path.insert(0, config.project_path + 'orientir/orientir')
#путь​ к виртуальному окружению myenv
sys.path.insert(0, config.project_path + 'orientir/myenv/lib/python3.6/site-packages')
os.environ["DJANGO_SETTINGS_MODULE"] = "orientir.settings"

import django
django.setup()

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()