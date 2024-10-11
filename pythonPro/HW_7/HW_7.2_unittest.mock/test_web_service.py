"""Використовуйте unittest.mock для макування HTTP-запитів. Замокуйте метод requests.get таким чином, щоб він
повертав фейкову відповідь (наприклад, {"data": "test"}), та протестуйте метод get_data.
Напишіть кілька тестів:
• перевірка успішного запиту (200)  • перевірка обробки помилки (404 чи інші коди)."""


import unittest
from unittest.mock import patch, Mock
from web_service import WebService


class TestWebService(unittest.TestCase):
    """Define a class that inherits from unittest.TestCase to use unittest's built-in methods for testing."""

    # Mock the requests.get() - replace this call with a mock object.
    # All requests.get() calls in the test will be intercepted and replaced with a fake (wet) object.
    @patch("requests.get")
    def test_get_data_success(self, mock_get):
        """The method receives a mock_get argument that will replace requests.get during the test."""

        mock_response = Mock()  # Simulates the response of an HTTP request.
        mock_response.status_code = 200  # Simulate status_code.
        mock_response.json.return_value = {"data": "test"}  # Simulate JSON data.

        # Set that when requests.get (replaced by mock_get) is called, it will return a fake mock_response
        # simulating a successful HTTP response.
        mock_get.return_value = mock_response

        # Create an instance of the class
        service = WebService()

        # Call the get_data method of the service object. Since in this test request.get is replaced by a mock object,
        # no real request is sent. Instead, a pre-prepared fake response is returned.
        result = service.get_data("https://callands-warrington.secure-dbprimary.com/warrington/primary/callands")
        # Check that the result of the get_data method call is equal to the expected value {‘data’: ‘test’}.
        self.assertEqual(result, {"data": "test"})

    @patch("requests.get")  # replace requests.get with mock-object.
    def test_get_data_404(self, mock_get):
        mock_response = Mock()  # Simulates the response of an HTTP request.
        mock_response.status_code = 404  # Simulate status_code.

        # Assign a fake response to the mock object.
        mock_get.return_value = mock_response

        # Create an instance of the class
        service = WebService()

        # Call the get_data method and check the result
        result = service.get_data("https://callands-warrington.secure-dbprimary.com/warrington/primary/callands")
        self.assertEqual(result, {"error": "Request failed with status 404"})


if __name__ == "__main__":
    unittest.main()
