from django.shortcuts import render
from django.http import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {
        "latest_question_list":latest_question_list
    }
    return render(request,'polls/index.html',context)
    

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('The question does not exist')
    return render(request, 'polls/detail.html',{"question": question.question_text})

def results(request, question_id):
    response = "You are looking at the results for question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." % question_id)


# Alternative code

# from django.http import HttpResponse

# from django.template import loader

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     template = loader.get_template('polls/index.html')
#     context = {
#         "latest_question_list":latest_question_list
#     }

#     return HttpResponse(template.render(context,request))