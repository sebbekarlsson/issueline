from issueline.IssueManager import IssueManager


manager = IssueManager('issueline/tests')


def test_report_issue():
    manager.write_data('issues', [])
    kind = 'bug'
    title = 'this is an issue'
    description = 'this is the description of the issue'
    author = 'unit-test'

    issue = manager.report_issue(kind, title, description, author)

    assert issue is not None
    assert issue.kind == kind
    assert issue.title == title
    assert issue.description == description
    assert issue.author == author
    assert issue.id is not None
