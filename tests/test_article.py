import unittest
from app.model import Article


class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Article class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Article('Kevin Kittony','Big change in Kenya','get the tips to making big changes','https://newsapi.org/v2/image','2019-04-12,', 'https://newsapi.org/v2/bigchanges')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))