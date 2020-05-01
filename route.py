# -*- coding: utf-8 -*-
from app import app
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension( app )


from interceptors.Auth import *
from interceptors.errorHandler import *

"""
blueprint
"""
from controllers.index import index_page

app.register_blueprint( index_page, url_prefix = "/" )

'''
Global template functions
'''
from common.libs.url_manager import UrlManager
app.add_template_global( UrlManager.build_static_url, 'buildStaticUrl' )
app.add_template_global( UrlManager.build_url, 'buildUrl' )