from flask import Flask
from flask_restful import reqparse, Resource, abort, Api
from app import spam as spm
from app import app_resources
from app.simple_spam_transformer import SimpleSpamTransformer

app = Flask(__name__)
api = Api(app)


parser = reqparse.RequestParser()
parser.add_argument('content')


@api.resource('/spam', resource_class_args=(app_resources.spam,))
class Spam(Resource):
    def __init__(self, spam: spm.Spam):
        self._spam = spam

    def post(self):
        args = parser.parse_args()
        message = args['content']
        self.abort_if_no_content(message)

        new_spam_id = self._spam.add_message(message)

        resp = api.make_response({'id': new_spam_id, 'content': message}, 201)
        resp.headers.extend({'Location': '/spam/' + new_spam_id})

        return resp

    @staticmethod
    def abort_if_no_content(message):
        if message is None:
            abort(400, message="Content field is not specified")


@api.resource('/ham/<ham_id>', resource_class_args=(app_resources.spam, app_resources.transformer))
class Ham(Resource):
    def __init__(self, spam: spm.Spam, transformer: SimpleSpamTransformer):
        self._spam = spam
        self._transformer = transformer

    def get(self, ham_id):
        self.abort_if_ham_doesnt_exist(ham_id)

        message = self._spam.get_message(ham_id)
        ham, success = self._transformer.transform(message)
        return {'content': ham, 'success': success}

    def abort_if_ham_doesnt_exist(self, ham_id):
        if ham_id not in self._spam.message_ids():
            abort(404, message="Ham {} doesn't exist".format(ham_id))


@api.resource('/spam/<ham_id>/ham', resource_class_args=(app_resources.spam, app_resources.transformer))
class HamOfSpam(Ham):
    def __init__(self, spam: spm.Spam, transformer: SimpleSpamTransformer):
        super(HamOfSpam, self).__init__(spam, transformer)


if __name__ == '__main__':
    app.run()
