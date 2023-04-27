import openai
import os
import dotenv
from django.http import JsonResponse
from django.shortcuts import render

dotenv.load_dotenv('.env')


def chatbot(request):
    prompt = request.POST.get('prompt', '')
    openai.api_key = os.environ['API_KEY']
    response = openai.Completion.create(
        engine='davinci',
        prompt=prompt,
        temperature=0.5,
        max_tokens=50,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    message = response.choices[0].text.strip()
    return JsonResponse({'message': message})


def chat(request):
    return render(request, 'new_site/chat.html')
