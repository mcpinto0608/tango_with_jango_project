import os
from re import L
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url': 'http://docs.python.org/3/tutorial/',
        'views': '30',
        'likes': '12'},
        {'title': 'How to Think like a Computer Scientist',
        'url': 'http://www.greenteapress.com/thinkpython/',
        'views': '34',
        'likes': '20'},
        {'title': 'Learn Python in 10 Minutes',
        'url': 'http://www.korokithakis.net/tutorials/python/',
        'views': '59',
        'likes': '27'}
    ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views':'34',
        'likes': '20'},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'views': '30',
        'likes': '12'},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'views': '59',
        'likes': '27'}
    ]

    other_pages = [
       {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views': '10',
        'likes': '50'},
       {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': '13',
        'likes': '5'} 
    ]

    cats = {'Python': {'pages': python_pages,'views': '128','likes': '64'},
            'Django': {'pages': django_pages, 'views': '64', 'likes': '32'},
            'Other Frameworks': {'pages': other_pages, 'views': '32', 'likes': '16'} }

    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data['views'],cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c,p['title'], p['url'],p['views'], p['likes'])
            

    
    for c in Category.objects.all():
        for p in Page.objects.filter(category = c):
            print(f'- {c}: {p}')
    
def add_page(cat, title, url, views = 0, likes = 0):
    p = Page.objects.get_or_create(category = cat, title = title)[0]
    p.url = url
    p.views = views
    p.likes = likes
    p.save()
    return p

def add_cat(name, views = 0, likes = 0):
    c = Category.objects.get_or_create(name = name)[0]
    c.views = views
    c.likes = likes
    # get_or_create returns a tuple(object,created) and the [0] at the end 
    # references the object only
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()