from flask import Blueprint, render_template, request


validate_endpoint = Blueprint("validate_endpoint", __name__)

@validate_endpoint.route("/add-post-validate", methods=['POST'])
def login_validate():
    forms = request.form
    data = forms.to_dict()
    user = data.get("input-email", None)
    pwd = data.get("input-pwd", None)
    if user != "AD@Jet01" or pwd != "jjjjjj":
        return "Login failed!"

    return render_template('add.html')