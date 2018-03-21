
import os
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5$3!+!9vz9=&$qczzd-l66_2a7gxc6w-zq%u90(4tlmyuu(&)i'


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES_LOCAL = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
}
DATABASES_DATABASES_PROD = {
    'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
}
