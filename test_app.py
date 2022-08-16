import unittest
from db import dal
from app import get_orders_by_customer


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        dal.db_init('sqlite:///:memory:')
        prep_db()

    def test_orders_by_customer_blank(self):
        results = get_orders_by_customer('')
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_shipped(self):
        results = get_orders_by_customer('', True)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_notshipped(self):
        results = get_orders_by_customer('', False)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_details(self):
        results = get_orders_by_customer('', details=True)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_shipped_details(self):
        results = get_orders_by_customer('', True, True)
        self.assertEqual(results, [])

    def test_orders_by_customer_blank_notshipped_details(self):
        results = get_orders_by_customer('', False, True)
        self.assertEqual(results, [])

    def test_orders_by_customer_bad_cust(self):
        results = get_orders_by_customer('bad name')
        self.assertEqual(results, [])

    def test_orders_by_customer_bad_cust_shipped(self):
        results = get_orders_by_customer('bad name', True)
        self.assertEqual(results, [])

    def test_orders_by_customer_bad_cust_notshipped(self):
        results = get_orders_by_customer('bad name', False)
        self.assertEqual(results, [])

    def test_orders_by_customer_bad_cust_details(self):
        results = get_orders_by_customer('bad name', details=True)
        self.assertEqual(results, [])

    def test_orders_by_customer_bad_cust_shipped_details(self):
        results = get_orders_by_customer('bad name', True, True)
        self.assertEqual(results, [])

    def test_orders_by_customer_bad_cust_notshipped_details(self):
        results = get_orders_by_customer('bad name', False, True)
        self.assertEqual(results, [])

    def test_orders_by_customer(self):
        results = get_orders_by_customer('cookiemon')
        self.assertEqual(results, self.cookie_orders)

    def test_orders_by_customer_shipped_only(self):
        results = get_orders_by_customer('cookiemon', True)
        self.assertEqual(results, [])

    def test_orders_by_customer_unshipped_only(self):
        results = get_orders_by_customer('cookiemon', False)
        self.assertEqual(results, self.cookie_orders)

    def test_orders_by_customer_with_details(self):
        results = get_orders_by_customer('cookiemon', details=True)
        self.assertEqual(results, self.cookie_details)

    def test_orders_by_customer_shipped_only_with_details(self):
        results = get_orders_by_customer('cookiemon', True, True)
        self.assertEqual(results, [])

    def test_orders_by_customer_unshipped_only_details(self):
        results = get_orders_by_customer('cookiemon', False, True)
        self.assertEqual(results, self.cookie_details)
