# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/home/w/weblocnw/weblocnw.beget.tech/public_html')
sys.path.insert(1, '/home/w/weblocnw/.local/lib/python2.7/site-packages/')

os.environ['DJANGO_SETTINGS_MODULE'] = 'main.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
