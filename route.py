# -*- coding: utf-8 -*-
from app import app
from flask_debugtoolbar import DebugToolbarExtension

toolbar = DebugToolbarExtension( app )


"""
blueprint
"""
from controllers.index import index_page
app.register_blueprint( index_page, url_prefix = "/" )

from controllers.about import about_page
app.register_blueprint(about_page, url_prefix ="/")

from controllers.login import login_page
app.register_blueprint(login_page, url_prefix="/")

from controllers.add_post_valuedate import validate_endpoint
app.register_blueprint(validate_endpoint, url_prefix="/")

from controllers.addpost import add_post_endpoint 
app.register_blueprint(add_post_endpoint, url_prefix="/")

from controllers.posts import post_page
app.register_blueprint(post_page, url_prefix="/")

'''
Global template functions
'''
# from common.libs.url_manager import UrlManager
# app.add_template_global( UrlManager.build_static_url, 'buildStaticUrl' )
# app.add_template_global( UrlManager.build_url, 'buildUrl' )