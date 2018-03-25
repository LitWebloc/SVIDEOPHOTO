# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/g/gorsin4h/gorsin4h.beget.tech/public_html/main/')
sys.path.insert(1, '/home/g/gorsin4h/.local/lib/python2.7/site-packages/')
os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
