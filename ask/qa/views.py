from django.shortcuts import render
from django.http import HttpResponse

from .models import Question, Author, Answer

from django.core.paginator import Paginator
from django.http import Http404
import forms


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    questions = Question.objects.order_by('-added_at')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'index.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def popular(request):
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    return render(request, 'popular.html', {
            'questions': page.object_list,
            'paginator': paginator,
            'page': page,
    })


def question(request, id):
    try:
        qst = Question.objects.get(pk=id)
    except Question.DoesNotExist:
        raise Http404
    answers = Answer.objects.filter(question=qst)
    answers = answers[:]
    form = forms.AnswerForm(initial={'question_id': id})
    return render(request, 'question.html', {
        'qst': qst,
        'answers': answers,
        'form': form,
    })

