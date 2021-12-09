from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404

# Create your views here.

def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date = dt.date.today()
    return render(request, 'all-news/today-news.html', {"date": date,})


def past_days_news(request,past_date):
    
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        day = convert_dates(date)
        html = f'''
            <html>
                <body>
                    <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
                </body>
            </html>
                '''
        return HttpResponse(html)