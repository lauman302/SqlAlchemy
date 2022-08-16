import unittest
from db import dal
from app import get_orders_by_customer


class TestApp(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        dal.db_init('sqlite:///:memory:')
    
    def test_orders_by_customer_blank(self):
        results = get_orders_by_customer('')
        self.assertEqual(results, [])
    
    def test_orders_by_customer_blank_shiped(self):
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
