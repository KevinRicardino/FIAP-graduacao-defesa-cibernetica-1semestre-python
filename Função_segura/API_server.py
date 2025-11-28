from flask import Flask
from flask_restful import Api, Resource
app = Flask(__name__)
api = Api(app)

class main(Resource):
    def get(self):
        msg = "Ola mundo"
        return msg
    def post(self):
        msg = "Ola mundo"
        return msg

class aluno(Resource):
    def get(self, nome):
        msg = "Ola " + nome
        return msg

api.add_resource(main, "/")
api.add_resource(aluno, "/aluno/<nome>")

if __name__ == "__main__":
    app.run()