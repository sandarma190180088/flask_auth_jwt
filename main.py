from flask import Flask,request,make_response,jsonify
from flask_restful import Api,Resource
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'fasisme'

class Login(Resource):
    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')

        if username and password == '12345':
            token = jwt.encode(
                        {
                            "username":username,
                            "exp":datetime.utcnow()+timedelta()
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

api.add_resource(Login,"/api/login")

if __name__ == "__main__":
    app.run(debug=True)
