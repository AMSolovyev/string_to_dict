from formatted_string import get_raw_string
import unittest


class TestGetRawString(unittest.TestCase):

    def test_check_digit_to_be_Equal(self):
        string = '{"6565":5345}'
        self.assertEqual(get_raw_string(string), {"6565": 5345})

    def test_check_digit_and_symbol_are_Equal(self):
        string = '{"fsg":67, "kkv":876}'
        self.assertEqual(get_raw_string(string), {"fsg": 67, "kkv": 876})

    def test_check_False(self):
        string = '{}'
        self.assertFalse(get_raw_string(string))

    def test_check_None(self):
        string = (456, 858)
        self.assertIsNone(get_raw_string(string))

    def test_check_None2(self):
        string = ['cat', 'dog']
        self.assertIsNone(get_raw_string(string))


if __name__ == '__main__':
    unittest.main()
