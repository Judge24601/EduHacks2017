from django.shortcuts import render
from django.url import resolve
from django.http import HttpRequest
import models


# Create your views here.
class questionView():
    def get(self, request):
        #role = !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        role = 'student'
        assignment_id, question_id = resolve(request.path)
        if role == 'student' :
            #assignment = StudentAssignment.objects.filter(student_assignment_id)
            question = StudentQuestion.objects.filter(question_id)
        elif role == 'instructor':
            #assignment = InstructorAssignment.objects.filter(instructor_assignment_id)
            question = InstructorQuestion.objects.filter(question_id)
        forum_posts = Forum_Posts.objects.filter(InstructorQuestion.instructor_question_id)
        return render(request, 'templates/questionView.html', {
            question, question.parent_question, forum_posts
        }, content_type='application/xhtml+xml')

    de
