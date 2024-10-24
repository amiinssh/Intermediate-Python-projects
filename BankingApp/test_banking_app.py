import unittest
from unittest.mock import patch
from online_banking_app import signIn, logIn, forgetPIN

class TestBankingApp(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['JohnDoe', '123456'])
    @patch('builtins.print')
    def test_sign_in_valid(self, mock_print, mock_input):
        """Test valid sign-in process with a 6-digit pin"""
        signIn()
        self.assertEqual(name, 'JohnDoe')
        self.assertEqual(pin, '123456')
        mock_print.assert_called_with("Thanks for creating your bank account")

    @patch('builtins.input', side_effect=['JohnDoe', '1234', '123456'])
    @patch('builtins.print')
    def test_sign_in_invalid_pin(self, mock_print, mock_input):
        """Test sign-in with invalid pin (less than 6 digits) and retry"""
        signIn()
        self.assertEqual(name, 'JohnDoe')
        self.assertEqual(pin, '123456')  
        mock_print.assert_any_call("Invalid pin. It has to be 6 digits")

    @patch('builtins.input', side_effect=['JohnDoe', 'wrongpin'])
    @patch('builtins.print')
    def test_login_wrong_pin(self, mock_print, mock_input):
        """Test logging in with wrong pin"""
        global name, pin
        name = "JohnDoe"
        pin = "123456"  
        logIn()
        mock_print.assert_any_call("Your username or your PIN is wrong, did you create an account?")

    @patch('builtins.input', side_effect=['newpin123', '123456'])
    @patch('builtins.print')
    def test_forget_pin(self, mock_print, mock_input):
        """Test forgetPIN process and create a new PIN"""
        global pin
        pin = "123456"
        forgetPIN()
        self.assertEqual(pin, '123456')
        mock_print.assert_any_call("The new PIN has been stored, please log in")

if __name__ == '__main__':
    unittest.main()
