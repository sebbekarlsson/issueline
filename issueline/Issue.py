import base64


class Issue(object):

    def __init__(self, kind, title, description=None, author=None, id=None):
        self.kind = kind
        self.title = title
        self.description = description
        self.author = author
        self.id = base64.b64encode(
            str(self.kind) +
            str(self.title) +
            str(self.description) +
            str(self.author)
        ) if not id else id

    def export(self):
        return self.__dict__
