import json
import os
from issueline.constants import ISSUE_DIRECTORY
from issueline.Issue import Issue


class IssueManager(object):

    def __init__(self, directory):
        self.directory = directory

        if not os.path.isdir(ISSUE_DIRECTORY):
            os.makedirs(ISSUE_DIRECTORY)

    def get_data(self, name):
        contents = None

        data_path = os.path.join(self.directory, ISSUE_DIRECTORY, name)\
            + '.json'

        if os.path.isfile(data_path):
            with open(data_path) as _file:
                contents = _file.read()
            _file.close()

        return json.loads(contents) if contents else []

    def write_data(self, name, data):
        data_path = os.path.join(self.directory, ISSUE_DIRECTORY, name)\
            + '.json'

        with open(data_path, 'w+') as _file:
            _file.write(json.dumps(data))
        _file.close()

        return self.get_data(name)

    def get_issues(self):
        return [Issue(**issue) for issue in self.get_data('issues')]

    def report_issue(self, kind, title, description, author):
        existing_data = self.get_data('issues')
        existing_data.append(Issue(
            kind=kind,
            title=title,
            description=description,
            author=author
        ).export())

        self.write_data('issues', existing_data)
