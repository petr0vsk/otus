import os
from flask import Flask
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
csrf = CSRFProtect(app)



app.config.update(dict(
    SECRET_KEY="4b332#@@1!74-006b-4889-8#@#-67b#@#b90ddffd",
    WTF_CSRF_SECRET_KEY='8207bece0139#4980!af20a681e3bf56f3',
   
))


from .home.views import *
from .views import *

