"""
WSGI config for IRWeb project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import lucene

from django.core.wsgi import get_wsgi_application
print("in wsgi file")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IRWeb.settings')
# if lucene.getVMEnv()==None:
#     # lucene.initVM(vmargs=['-Djava.awt.headless=true'])
#     lucene.initVM(lucene.CLASSPATH)
# lucene.getVMEnv().attachCurrentThread()




application = get_wsgi_application()
