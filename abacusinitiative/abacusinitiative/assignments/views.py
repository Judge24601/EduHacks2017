from django.shortcuts import render
from django.url import reverse, resolve
from django.http import HttpRequest, HttpResponse
import models.py


# Create your views here.
class questionView(View):
    def get(self, request):
        role = !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        assignmentID, questionID = resolve(request)
        if role == 'student' :
            #assignment = StudentAssignment.objects.filter(student_assignment_id)
            question = StudentQuestion.objects.filter(student_question_id)
        elif role == 'instructor'
            #assignment = InstructorAssignment.objects.filter(instructor_assignment_id)
            question = InstructorQuestion.objects.filter(instructor_question_id)
        return question
