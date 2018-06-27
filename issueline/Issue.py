import base64
import datetime


class Issue(object):

    def __init__(
        self,
        kind,
        title,
        description=None,
        author=None,
        id=None,
        date=None
    ):
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
        self.date = datetime.datetime.now() if not date else date

    def export(self):
        return self.__dict__
