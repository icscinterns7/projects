from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.


monthly_challenges = {
    'january': 'Learn C',
    'february': 'Learn CPP',
    'march': 'Learn Java',
    'april': 'Learn PHP',
    'may': 'Learn Python',
    'june': 'Learn Django',
    'july': 'Learn GraphQL',
    'august': 'Learn RestFullAPI',
    'september': 'Learn Git and GitHub',
    'october': 'Learn Docker',
    'november': 'Learn AWS',
    'december': None,
}


def index(request):
    # list_items = ''
    months = list(monthly_challenges.keys())

    # for month in months:
    #     captalized_month = month.capitalize()
    #     month_path = reverse('month-challenge', args=[month])
    #     list_items += f"<li><a href=\"{month_path}\">{captalized_month}</a></li>"
    # response_data = f'<ul>{list_items}</ul>'
    # return HttpResponse(response_data)

    return render(request, 'challenges/index.html', {'months': months})


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month.</h1>')
    redirect_month = months[month - 1]
    redirect_path = reverse(
        'month-challenge', args=[redirect_month])  # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        # response_data = f'<h1>{challenge_text}</h1>'
        # response_data = render_to_string('challenges/challenge.html')
        # return HttpResponse(response_data)
        return render(request, 'challenges/challenge.html', {'text': challenge_text, 'month_name': month})
    except:
        raise Http404()
