import hashlib
from flask import Blueprint, render_template, request, make_response
from app import app
from common.db_models.user import User


validate_endpoint = Blueprint("validate_endpoint", __name__)

@validate_endpoint.route("/add-post-validate", methods=['POST', "GET"])
def login_validate():

    if request.method == "GET":
        cookie = request.cookies.get(app.config["AUTH_COOKIE_NAME"])
        user_id = str(cookie).split("#")[-1]
        user_info = User.query.filter_by(id=user_id).first()
        if not user_info:
            return login_failed()
        pwd = user_info.password
        digest = gen_digest(pwd=pwd)
        if str(digest) != str(cookie).split("#")[0]:
            return login_failed()
        return render_template("add.html")

    forms = request.form
    data = forms.to_dict()
    user = data.get("input-email", None)
    pwd = data.get("input-pwd", None)

    user_info = User.query.filter_by(user_name = user).first()
    if not user_info:
        return login_failed()

    if user_info.user_name != user:
        return login_failed()

    if user_info.password != pwd:
        return login_failed()

    digest = gen_digest(pwd=pwd)

    response = make_response(render_template('add.html'))
    response.set_cookie(app.config["AUTH_COOKIE_NAME"], "%s#%s" % (digest, user_info.id), 60*20)

    return response


def login_failed():
    return "Login failed!"

def gen_digest(pwd):
    auth_code = app.config["AUTH_CODE"]
    m = hashlib.md5()
    m.update(str(auth_code).encode('utf-8') + str(pwd).encode("utf-8"))

    return m.digest()