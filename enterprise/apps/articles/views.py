from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from .models import Article, Comment, Subject, Test_case, Test
from django.urls import reverse
from sphere_engine import ProblemsClientV4
from sphere_engine.exceptions import SphereEngineException


subjects_list = Subject.objects.order_by('subject_name')


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]
    #one_subject = Subject.objects.get(id=subject_id)
    return render(request, 'articles/list.html',{'latest_articles_list': latest_articles_list , 'subjects_list': subjects_list})


def detail(request, article_id):
    try:
        a = Article.objects.get( id = article_id)
    except:
        raise Http404("Стаття не знайдена")
    latest_comments_list = a.comment_set.order_by('-id')[:10]


    return render(request, 'articles/detail.html', {'article': a, 'latest_comments_list': latest_comments_list,  'subjects_list': subjects_list})

def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id=article_id)
    except:
        raise Http404("Стаття не знайдена")

    a.comment_set.create(author_name=request.POST['name'], comment_text=request.POST['text'])

    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,)))


def sub_list(request):
    return render(request, 'subjects/sub_list.html', {'subjects_list': subjects_list})


def sub_detail(request, subject_id):
    try:
        b = Subject.objects.get(id=subject_id)
    except:
        raise Http404("Предмет не знайдений")
    #test_case_list = Test_case.objects.order_by('-id')

    latest_tests = b.test_case_set.order_by('-id')
    return render(request, 'subjects/sub_detail.html', {'subject': b, 'latest_tests': latest_tests, 'subjects_list': subjects_list})


def contacts(request):
    return render(request, 'contacts/contacts.html', {'subjects_list': subjects_list})


def personal_page(request):
    current_user = request.user
    return render(request, 'personal_page/personal_page.html', {'user': current_user, 'subjects_list': subjects_list})


def test_case(request, test_case_id):
    try:
        b = Test_case.objects.get(id=test_case_id)
    except:
        raise Http404("Тестова робота не знайдена")

    return render(request, 'test/test_detail.html', {'test_case': b, 'subjects_list': subjects_list})

def done(request):


    return render(request, 'test/done.html', {'subjects_list': subjects_list})


def testing(request, test_case_id):
    try:
        b = Test.objects.get(test_case_id=test_case_id)
    except:
        raise Http404("Завдання не знайдені")

    test_time = b.test_case.case_duration * 60

    accessToken = '82c0c5507c39a743ef533af852e97b11'
    endpoint = 'd32fffd4.problems.sphere-engine.com'

    client = ProblemsClientV4(accessToken, endpoint)

    problemId = b.sphere_id

    try:
        response = client.problems.get(problemId)
    except SphereEngineException as e:
        if e.code == 401:
            print('Invalid access token')
        elif e.code == 403:
            print('Access to the problem is forbidden')
        elif e.code == 404:
            print('Problem does not exist')

    return render(request, 'test/test.html', {'test_case': b, 'subjects_list': subjects_list, 'response': response, 'test_time': test_time})
