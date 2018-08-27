from formatted_string import get_raw_string, get_converted_dict
import unittest


class TestGetRawString(unittest.TestCase):

    def test_check_digit_to_be_Equal(self):
        string = '{"6565":122}'
        self.assertEqual(get_converted_dict(string), {"6565":122})

    def test_check_digit_and_symbol_are_Equal(self):
        string = '{"fsg":67, "kkv":876}'
        self.assertEqual(get_converted_dict(string), {"fsg": 67, "kkv": 876})

    def test_check_None(self):
        string = '{}'
        self.assertFalse(get_converted_dict(string))

    def test_check_NotNone(self):
        string = '["cat", "dog"]'
        self.assertIsNotNone(get_converted_dict(string))
 
if __name__ == '__main__':
    unittest.main()
