from django.shortcuts import render
def startpage(request):
return render(request, "quiz/startpage.html")
def quiz(request):
return render(request, "quiz/quiz.html")
def question(request):
return render(request, "quiz/question.html")
def completed(request):
return render(request, "quiz/completed.html")
from django.shortcuts import render

# Create your views here.
