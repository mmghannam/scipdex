from io import StringIO
from unittest.mock import patch

@patch('sys.stdout', new_callable=StringIO)
def test_print_version(mock_stdout):
    from print_version import print_version

    print_version()
    assert "SCIP version" in mock_stdout.getvalue(), "SCIP version is not printed to stdout"
