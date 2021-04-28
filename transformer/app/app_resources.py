from app.simple_spam_transformer import SimpleSpamTransformer
from app.spam import SpamIDServer, Spam

spam_id_server = SpamIDServer()
spam = Spam(spam_id_server)

transformer = SimpleSpamTransformer()
