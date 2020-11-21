from simple_spam_transformer import SimpleSpamTransformer
from spam import SpamIDServer, Spam

spam_id_server = SpamIDServer()
spam = Spam(spam_id_server)

transformer = SimpleSpamTransformer()
