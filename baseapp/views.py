from django.shortcuts import render, redirect
from . import practice, speed
# Create your views here.

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

content_text = practice.get_content()
context = {
    "content_text": content_text ,
    "typing_speed": "0 WPM"
}

@csrf_exempt
def home(request):
    # content_text = practice.get_content()

    if request.method == 'POST':
        print('***************************************************************************')
        # content_text = 'demo text222222 for testing in english '

        data = json.loads(request.body)
        first_keypress_timestamp = data.get('first_keypress_timestamp')
        submit_timestamp = data.get('submit_timestamp')
        content = data.get('content')

        # You can now use the timestamps and content
        # Save them to your database or perform other actions
        typing_speed = speed.calculate_typing_metrics(content_text,content,first_keypress_timestamp,submit_timestamp)
        context['content_text'] = practice.get_content()
        context['typing_speed'] = typing_speed


        return redirect('home')


    return render(request, 'index.html',context)

