#assertEqual(A,B)
# assert A==B

# assertTrue(A)
# assert A is True

# assertIn(A,B)
# assert A in B

# assertNotEqua(A,B)
# assert A!=B

# assertFalse(A,B)
# assert A is False

# assertNotIn(A,B)
# assert A not in B

import unittest
from shopping_list import ShoppingList

class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"纸巾": 8, "帽子": 30, "拖鞋": 15})

    def test_get_item_count(self):
        self.assertEqual(self.shopping_list.get_item_count(), 3)

    def test_get_total_price(self):
        self.assertEqual(self.shopping_list.get_total_price(), 53)

        
#打开终端，输入：python -m unittest
#两个点表示两个都没错  


