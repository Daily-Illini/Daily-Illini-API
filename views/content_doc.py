from flask import Blueprint, render_template, request
from flask_cors import cross_origin
from google.oauth2 import id_token
from google.auth.transport import requests

from util.security import csrf

contentdoc_routes = Blueprint("contentdoc_routes", __name__, url_prefix="/contentdoc")


@cross_origin()
@csrf.exempt
@contentdoc_routes.route("/verifytoken", methods=["POST"])
def verifytoken():
    token = request.form["token"]
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request())
        email = idinfo["email"]
        if email.endswith("@illinimedia.com"):
            return "Valid", 200
        else:
            return "Valid token but email is not from @illinimedia.com", 401
    except ValueError:
        return "Invalid token", 401
