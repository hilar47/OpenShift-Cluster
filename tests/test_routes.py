"""Unit tests for the counter service."""
from unittest import TestCase

from service import app
from service.routes import COUNTERS


class CounterTest(TestCase):
    """Counter service tests."""

    def setUp(self):
        """Create a fresh client and clear state."""
        self.client = app.test_client()
        COUNTERS.clear()

    def test_index(self):
        """It should return service info"""
        resp = self.client.get("/")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["name"], "Counter Service")

    def test_health(self):
        """It should report healthy"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["status"], "OK")

    def test_create_counter(self):
        """It should create a counter at zero"""
        resp = self.client.post("/counters/foo")
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(resp.get_json()["foo"], 0)

    def test_duplicate_counter(self):
        """It should not create a duplicate counter"""
        self.client.post("/counters/foo")
        resp = self.client.post("/counters/foo")
        self.assertEqual(resp.status_code, 409)

    def test_list_counters(self):
        """It should list counters"""
        self.client.post("/counters/foo")
        resp = self.client.get("/counters")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("foo", resp.get_json())

    def test_read_counter(self):
        """It should read a counter"""
        self.client.post("/counters/foo")
        resp = self.client.get("/counters/foo")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["foo"], 0)

    def test_read_missing_counter(self):
        """It should return 404 for a missing counter"""
        resp = self.client.get("/counters/nope")
        self.assertEqual(resp.status_code, 404)

    def test_update_counter(self):
        """It should increment a counter"""
        self.client.post("/counters/foo")
        resp = self.client.put("/counters/foo")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["foo"], 1)

    def test_update_missing_counter(self):
        """It should return 404 when updating a missing counter"""
        resp = self.client.put("/counters/nope")
        self.assertEqual(resp.status_code, 404)

    def test_delete_counter(self):
        """It should delete a counter"""
        self.client.post("/counters/foo")
        resp = self.client.delete("/counters/foo")
        self.assertEqual(resp.status_code, 204)
        self.assertEqual(self.client.get("/counters/foo").status_code, 404)
