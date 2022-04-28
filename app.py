import os
from flask import Flask, request, jsonify, make_response, send_from_directory
from flask_restful import Resource, Api, reqparse
from flask_cors import CORS, cross_origin
from flask import render_template

# from flask_jwt_extended import create_access_token
# from flask_jwt_extended import get_jwt_identity
# from flask_jwt_extended import jwt_required
# from flask_jwt_extended import JWTManager
# from flask_jwt_extended import set_access_cookies
# from flask_jwt_extended import unset_jwt_cookies

app = Flask(__name__)
# app.config["JWT_TOKEN_LOCATION"] = ["headers"] # options: "cookies", "json", "query_string"
# app.config["JWT_COOKIE_SECURE"] = True # only allow the cookies that contain your JWTs to be sent over https
# app.config["JWT_COOKIE_SAMESITE"] = "None"
# app.config["JWT_SECRET_KEY"] = "super-secret-jfi;l_8"
app.secret_key = 'keyyyyyyyyyyy-y^%#M.'
app.config['CORS_HEADERS'] = 'Content-Type'
whitelist = ['http://localhost:3000', 'http://127.0.0.1:3000', 
	'https://127.0.0.1:3000', 'https://127.0.0.1:5000', "https://192.168.1.18:5000/",]
cors = CORS(app, 
	resources={r"/api": {"origins": whitelist}}, 
	supports_credentials=True) # https://flask-cors.readthedocs.io/en/latest/
api = Api(app)
# jwt = JWTManager(app)

# for test
# @app.route("/api/test", methods=['GET'])
# def test():
#     access_token = create_access_token(identity=str(1))
#     # Set cookie
#     response = jsonify(status='success')
#     response.set_cookie(
#         'access_token', access_token, 
#         domain=".app.localhost", 
#         path='/', 
#         max_age=600,
#         secure=True, 
#         httponly=False,
#         samesite="None"
#     )
#     return response

COOKIE_NAME = 'coookie'

class CookieTest(Resource):
	@cross_origin(origins="http://localhost:3000", supports_credentials=True)
	def get(self):
		request_cookie = request.cookies.get(COOKIE_NAME)
		response_body = {'Message': request_cookie}
		print('request_cookie:', request_cookie)

		response = jsonify(response_body)
		response.set_cookie(
			COOKIE_NAME, 'this_is_your_token', 
			domain="setcookie-backend.herokuapp.com", 
			path='/', 
			max_age=600,
			secure=True, 
			httponly=True,
			samesite="None"
		)
		return response

api.add_resource(CookieTest, '/api')

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5000, debug = True)