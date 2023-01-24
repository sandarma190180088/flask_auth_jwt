from flask import Flask,request,make_response,jsonify
from flask_restful import Api,Resource
from datetime import datetime, timedelta
import jwt
from functools import wraps


app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'fasisme'

def token_required(func):
    @wraps(func)
    def decorator(*args,**kwargs):
        token = request.args.get('token')
        if not token:
            return make_response(
                        jsonify(
                                {"msg":"not found token"}
                            )
                        ,404
                    )
        try:
            output = jwt.decode(token,app.config['SECRET_KEY'],
                                algorithms=['HS256'])
            return make_response(jsonify({
                    "output":output
                }),200)

        except Exception as e:
            return make_response(jsonify({
                    "msg":f'{e}'
                }),404)
    return decorator

class Login(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password == '12345':
            token = jwt.encode(
                        {
                            "username":username,
                            "exp":datetime.utcnow()+timedelta(minutes=2)
                        },app.config['SECRET_KEY'],algorithm="HS256"

                    )
            return jsonify({
                    "token":token,
                    "msg": "Anda Berhasil Login !",
                    "status": True
                })
        return jsonify({
                "msg":"silahkan Login !",
                "status": 0
            })

class Home(Resource):
    @token_required
    def get(self):
        return jsonify({
                "msg":"This is Home Page"
            })


api.add_resource(Login,"/api/login")
api.add_resource(Home,'/api')
if __name__ == "__main__":
    app.run(debug=True)
