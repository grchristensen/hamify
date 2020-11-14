from flask import Flask
from flask_restful import reqparse, abort, Resource, Api

from SimpleSpamTransformer import SimpleSpamTransformer

app = Flask(__name__)
api = Api(app)


def abort_if_ham_doesnt_exist(ham_id):
    if ham_id not in spam:
        abort(404, message="Ham {} doesn't exist".format(ham_id))


class SpamIDServer:
    def __init__(self):
        self._spam_id = 0

    def spam_id(self):
        self._spam_id += 1

        return str(self._spam_id)


spam = {}
id_server = SpamIDServer()
transformer = SimpleSpamTransformer()


parser = reqparse.RequestParser()
parser.add_argument('content')


class Spam(Resource):
    def post(self):
        args = parser.parse_args()
        new_spam_id = id_server.spam_id()
        spam[new_spam_id] = {'content': args['content']}
        return new_spam_id, 201


class Ham(Resource):
    def get(self, ham_id):
        abort_if_ham_doesnt_exist(ham_id)
        ham = transformer.transform(spam[ham_id]['content'])
        return {'content': ham}


api.add_resource(Spam, '/spam')
api.add_resource(Ham, '/ham/<ham_id>')


if __name__ == '__main__':
    app.run()
