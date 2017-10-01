from django.db import models
#from accounts.models import Student
#from accounts.models import Instructor
# Create your models here.
class StudentAssignment (models.Model):
    student_assignment_id = models.PositiveIntegerField(
        primary_key = True,
        db_index = True,
    )
    parent_assignment = models.ForeignKey(
        'InstructorAssignment',
        on_delete = models.CASCADE,
    )
    score = models.PositiveSmallIntegerField()

class InstructorAssignment (models.Model):
    instuctor_assignment_id = models.PositiveIntegerField(
        primary_key = True,
        db_index = True,
    )

class StudentQuestion (models.Model):
    student_question_id = models.PositiveIntegerField(
        primary_key = True,
        db_index = True,
    )
    ans_text = models.CharField(
        max_length = 255,
    )
    ans_num = models.FloatField()
    assignment = models.ForeignKey(
        'StudentAssignment',
        on_delete = models.CASCADE,
    )
    parent_question = models.ForeignKey(
        'InstructorQuestion',
        on_delete = models.CASCADE,
    )
    score = models.PositiveSmallIntegerField()

class InstructorQuestion (models.Model):
    instructor_question_id = models.PositiveIntegerField(
        primary_key = True,
        db_index = True,
    )
    correct_ans_text = models.CharField(
        max_length = 255,
    )
    correct_ans_num = models.FloatField()
    ans_type = models.CharField(
        max_length = 20,
    )
    text = models.TextField()

class Forum_Post(models.Model):
    forum_post_id = models.PositiveIntegerField(
        primary_key = True,
        db_index = True,
    )
    query = models.TextField()
    #poster = models.ForeignKey(
    #    'Student',
    #    on_delete = models.CASCADE,
    #)
    linked_q = models.ForeignKey(
        'InstructorQuestion',
        on_delete = models.CASCADE,
    )
    posts = models.Manager()

class Forum_Response(models.Model):
    forum_response_id = models.PositiveIntegerField(
        primary_key = True,
        db_index = True,
    )
    text = models.TextField();
    #poster = models.ForeignKey(
    #    'Student',
    #    on_delete = models.CASCADE,
    #)
    response_to = models.ForeignKey(
        'Forum_Post',
        on_delete = models.CASCADE,
    )

class Instructor_Response(models.Model):
    instructor_response_id = models.PositiveIntegerField(
        primary_key = True,
        db_index = True,
    )
    text = models.TextField();
    #poster = models.ForeignKey(
    #    'Instructor',
    #    on_delete = models.CASCADE,
    #)
    response_to = models.ForeignKey(
        'Forum_Post',
        on_delete = models.CASCADE,
    )
