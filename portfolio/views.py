from django.shortcuts import render
from .models import Profile, Skill, Work
import urllib.request
import json


def index(request):
    profile = Profile.objects.all().last()  # .last()で最後のデータを取得
    skills = Skill.objects.all()
    works = Work.objects.all().order_by('-published')[:3]

    context = {
        'profile': profile,
        'skills': skills,
        'works': works,
    }

    # レポジトリ使用言語取得（git api使用）
    lang_dict = {
        'Total': 0,
        'Python': 0,
        'PHP': 0,
        'JavaScript': 0,
        'Other': 0
    }
    url = 'https://api.github.com/users/Kyosuke-Fukui/repos?page=1&per_page=1000'
    with urllib.request.urlopen(url) as res:
        json_text = res.read().decode('utf-8')
        json_obj = json.loads(json_text)
    for repo in json_obj:
        lang_dict['Total'] += 1
        try:
            if ('Python' in repo['language']) or ('Jupyter Notebook' in repo['language']):
                lang_dict['Python'] += 1
            elif ('PHP' in repo['language']):
                lang_dict['PHP'] += 1
            elif ('JavaScript' in repo['language']):
                lang_dict['JavaScript'] += 1
            else:
                lang_dict['Other'] += 1
        except:
            lang_dict['Other'] += 1

    return render(request, 'index.html', {'context': context, 'lang_dict': lang_dict})
