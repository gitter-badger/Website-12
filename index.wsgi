import os
import sys

sys.path.append(os.path.dirname(__file__))
sys.path.insert(0, '/var/www/fsmbelgium.com/index.wsgi')

from index import app as application
