import unittest
from app import db
from app.models import Comment, Subscriber, Post
​
class CommentModelTest(unittest.TestCase):
    def setUp(self):
        self.user_john = User(username = 'john', password = 'king5555', email = 'j.yayah7@gmail.com')
        self.new_post = Post(id = 1, post_title = 'Test', post_content = 'This is a test post', category = 'health', user = self.user_john)
        self.new_comment = Comment(id = 1, comment = 'Test comment', user = self.user_john, post_id = self.new_post)