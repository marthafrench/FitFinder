import unittest
from app.chatbot import recommend_size

class TestChatbot(unittest.TestCase):
    
    def test_recommend_size(self):
        # Example test case
        result = recommend_size('10', 170, 'looser')
        self.assertEqual(result, 11)  # Expected size
        
    def test_invalid_size(self):
        result = recommend_size('not_a_size', 170, 'tight')
        self.assertEqual(result, None)  # Or handle appropriately
        
if __name__ == '__main__':
    unittest.main()
