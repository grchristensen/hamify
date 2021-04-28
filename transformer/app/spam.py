class SpamIDServer:
    def __init__(self):
        self._spam_id = 0

    def spam_id(self):
        self._spam_id += 1

        return str(self._spam_id)


class Spam:
    def __init__(self, id_server: SpamIDServer):
        self._id_server = id_server

        self._messages = {}

    def add_message(self, message: str) -> str:
        message_id = self._id_server.spam_id()

        self._messages[message_id] = message

        return message_id

    def get_message(self, message_id: str):
        return self._messages[message_id]

    def message_ids(self):
        return self._messages.keys()
