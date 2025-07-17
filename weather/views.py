from django.shortcuts import render
from django.http import JsonResponse
import requests
from django.views.decorators.csrf import csrf_exempt

# Your OpenWeatherMap API key here
API_KEY = '627e739338a21357be7d7e8dd1a7e8a2'

def index(request):
    # Render the main SPA page
    return render(request, 'weather/index.html')


@csrf_exempt  # only if you want to skip CSRF for AJAX POST; better to handle CSRF token properly in your JS
def get_weather(request):
    if request.method == 'POST':
        city = request.POST.get('city')

        if not city:
            return JsonResponse({'error': 'City name is required.'})

        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)

        if response.status_code != 200:
            return JsonResponse({'error': 'City not found or API error.'})

        data = response.json()

        weather_data = {
            'city': data.get('name'),
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'].capitalize(),
            'icon': data['weather'][0]['icon'],
        }
        return JsonResponse(weather_data)

    # If GET or other method, just return error
    return JsonResponse({'error': 'Invalid request method.'})
