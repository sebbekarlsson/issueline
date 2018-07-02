from issueline.IssueManager import IssueManager


manager = IssueManager('issueline/tests')


def test_get_data_issues():
    data = manager.get_data('issues')

    assert data is not None
    assert isinstance(data, list)
