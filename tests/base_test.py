from unittest import TestCase
from app import create_app

app = create_app("testing")


class BaseTest(TestCase):
    """Base class which is inherited by all system test classes."""

    request_headers = {"Content-Type": "application/json"}

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def setUp(self) -> None:
        """Create all db tables before each test."""
        self.client = app.test_client()
        self.app_context = app.app_context()

    def tearDown(self):
        """Clear db tables after each test"""
        pass
