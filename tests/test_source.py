import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Source(5467,'BBC Kenya','Bringing you the lastest news updates','politics','Kenya', 'https://newsapi.org/v2/sources')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))