from django.test import TestCase
from .db_services import DBchecker
from news.models import Comment, Job

# Create your tests here.


class TestDBCheckerService(TestCase):

    def setUp(self) -> None:
        self.db_checker = DBchecker()

    def test_tables_are_empty_returns_false(self):
        is_not_empty = self.db_checker.check_dbs()
        self.assertEqual(is_not_empty, False)

    def test_tables_with_data_returns_true(self):
        # Add a record to the Comment table
        comment = Comment(id=1, parent=0, by='Gunax',
                          text="This is required concept", time=1633544861, type='comment')
        comment.save()

        is_not_empty = self.db_checker.check_dbs()
        self.assertEqual(is_not_empty, True)


class TestDBWriterService(TestCase):

    def setUp(self) -> None:
        Comment.objects.create(id=1, parent=0, by='Gunax',
                               text="This is required concept", time=1633544861, type='comment')

    def test_comment_table_populated(self):
        comment = Comment.objects.get(id=1)
        self.assertEqual(comment.text, "This is required concept")
        self.assertEqual(comment.type, "comment")
        self.assertEqual(comment.deleted, False)

    def test_use_dict_to_populate_table(self):
        job_dict = {"id": 1, "title": "The Test", "by": "Gunar",
                    "text": "This is a test", "time": 163346732, "type": "job"}
        Job.objects.create(**job_dict)
        job = Job.objects.get(id=1)

        self.assertEqual(job.text, "This is a test")
        self.assertEqual(job.type, "job")
