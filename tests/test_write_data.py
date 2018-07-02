from issueline.IssueManager import IssueManager


manager = IssueManager('issueline/tests')


def test_write_data_issues():
    data = manager.write_data('issues', ['hello', 'world'])

    assert data is not None
    assert data == ['hello', 'world']
