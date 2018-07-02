from issueline.IssueManager import IssueManager


manager = IssueManager('issueline/tests')


def test_query_issue():
    manager.write_data('issues', [])
    kind = 'bug'
    title = 'this is an issue'
    description = 'this is the description of the issue'
    author = 'unit-test'

    issue = manager.report_issue(kind, title, description, author)

    queried_issue = manager.query({'id': issue.id}, True)

    assert queried_issue is not None
    assert queried_issue.kind == kind
    assert queried_issue.title == title
    assert queried_issue.description == description
    assert queried_issue.author == author
