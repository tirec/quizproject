from django.shortcuts import render
def startpage(request):
	context = {
		"quizzes": quizzes,
	}
	return render(request, "quiz/startpage.html", context)
def quiz(request, quiz_number):
	context = {
		"quiz": quizzes[int(quiz_number) - 1],
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/quiz.html", context)
def question(request, quiz_number, question_number):
	context = {
		"question_number": question_number,
	    "question": "Hur många bultar har Ölandsbron?",
		"answer1": "12",
	   	"answer2": "66 400",
	    "answer3": "7 428 954",
	    "quiz_number": quiz_number,
	}
	return render(request, "quiz/question.html", context)
def completed(request, quiz_number):
	context = {
	    "correct": 12,
	    "total": 20,
		"quiz_number": quiz_number,
	}
	return render(request, "quiz/completed.html", context)

quizzes = [
	{
		"quiz_number": 1,
   		"name": "Det ultimata Disney-quizet",
	   	"description": "Kan du dina disneyfilmer?"
	},
	{
		"quiz_number": 2,
   	   	"name": "Det här quizet ska du välja",
	   	"description": "För det har jag lagt extra mycket tid på."
	},
	{
		"quiz_number": 3,
   	    	"name": "Gissa bilden",
	    	"description": "Kan du se vad som döljer sig i bilderna?"	},
]

# Create your views here.
