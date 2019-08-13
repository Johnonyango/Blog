import unittest
from app.models import Comment, Subscriber, Post
from app import db
​
​
class PitchModelTest(unittest.TestCase):
    def setUp(self):
        self.user_john = User(
            username='john', password='king5555', email='j.yayah7@gmail.com')
        self.new_post = Post(id=1, post_title='Test', post_content='This is a test',
                               category="interview", user=self.user_john)
​
    def tearDown(self):
        Post.query.delete()
        User.query.delete()
​
    def test_check_instance_variables(self):
        self.assertEquals(self.new_post.post_title, 'Test')
        self.assertEquals(self.new_post.post_content, 'This is a test')
        self.assertEquals(self.new_post.post_category, "interview")
        self.assertEquals(self.new_post.user, self.user_john)
​
    def test_save_post(self):
        self.new_post.save_post()
        self.assertTrue(len(Post.query.all()) > 0)
​
    def test_get_pitch_by_id(self):
        self.new_post.save_post()
        get_post = Post.get_post(1)
        self.assertTrue(get_post is not None)