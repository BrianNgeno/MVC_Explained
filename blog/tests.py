from django.test import TestCase
from models import Blog
# Create your tests here.
class BlogTestClass(TestCase):
    """
    Test blog class and its functions
    """
    def setUp(self):
        #creating a new instance
        self.blog = Blog( time_created='2006-10-25',publisher='Brian Ngeno',title='informative', content='This is to explain on the MVC model', slug="mvc_framework_explained",image='blog_image.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.blog, Blog))
