from django.test import TestCase
from django.urls.base import reverse
from .models import Comment

# Create your tests here.


class CommentListViewTests(TestCase):

    def setUp(self) -> None:
        self.comment = Comment.objects.create(id=1, parent=0, by='Gunax',
                                              text="This is required concept", time=1633544861, type='comment')

    def test_comments_list_view(self):
        response = self.client.get(reverse('comments'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This is required concept")
        self.assertTemplateUsed(response, 'list.html')

    def test_records_are_sorted_descending(self):
        # Arrange
        Comment.objects.create(id=1, parent=0, by='Gunax',
                               text="This is required concept", time=1633544861, type='comment')
        Comment.objects.create(id=2, parent=0, by='Gunax',
                               text="This is required concept", time=1633544861, type='comment')

        # Call the view and check if sorted in descending order
        Comment.objects.order_by('-id')

        self.assertEqual(Comment.objects.first().id, 2)
