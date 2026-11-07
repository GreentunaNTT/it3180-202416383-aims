from aims.cart import Cart
import unittest

class TestCart(unittest.TestCase):
    def test_add_dvd_limit(self):
        """
        Kiểm tra thêm thành công 20 đĩa DVD vào giỏ hàng, 
        và phương thức add_dvd() trả về False khi thêm đĩa thứ 21.
        """
        
        cart = Cart()
        
        # 1. Thêm 20 đĩa DVD đầu tiên -> Yêu cầu trả về True (hoặc thành công)
        for i in range(1, 21):
            dvd = f"DVD_{i}"
            result = cart.add_dvd(dvd)
            self.assertTrue(result, f"Thêm đĩa thứ {i} thất bại nhưng kỳ vọng thành công.")
        
        # 2. Thêm đĩa DVD thứ 21 -> Phương thức add_dvd() phải trả về False
        extra_dvd = "DVD_21"
        result_21 = cart.add_dvd(extra_dvd)
        self.assertFalse(result_21, "Đĩa thứ 21 phải trả về False do vượt quá số lượng tối đa cho phép.")

if __name__ == '__main__':
    unittest.main()