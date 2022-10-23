"""
Module that will test certain aspects of the website.
More tests to be added as features are implemented.
"""
import requests  # used to send GET and POST requests to websites


class TestWebsite:
    """
    Construct the website tester
    """

    def __init__(self, _url="http://127.0.0.1:5000") -> None:
        """
        Parameters:
        _url: the url for the webapp, including port eg: 'http://127.0.0.1:5000'
        """
        self.url = _url

    def test_connection(self) -> None:
        """
        Test that the web app is running
        """
        try:
            print("Testing connection to the server:")
            response = requests.get(self.url)
            print("Website response code: " + str(response.status_code))
            assert response.status_code == 200  # 200 is a typical 'ok' response
        except:
            print("Testing server connections went wrong. Please send terminal output and create an issue on the github repository.")
        else:
            print("Connection test successful")

if __name__ == "__main__":
    """
    Run some tests if this file is run itself, and not through
    a module call.
    """
    website_tester = TestWebsite()
    website_tester.test_connection()
