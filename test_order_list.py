import unittest

from linear_list.order_list import OrderList


class TestOrderList(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_create_order_list(self):
        ol = OrderList()
        ol.create_list()
        print(ol)

