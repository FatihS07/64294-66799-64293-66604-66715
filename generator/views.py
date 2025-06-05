from datetime import timedelta
from django.shortcuts import render
from django.http import JsonResponse
import random
from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter
from datetime import timedelta
from .models import LottoDraw
from django.utils import timezone

def index(request):
    return render(request, 'generator/index.html')

def generate_numbers2(request):
    numbers = sorted(random.sample(range(1, 50), 6))
    return JsonResponse({'numbers': numbers})


# Django API Endpoint'leri
@api_view(['GET'])
def generate_numbers(request):
    numbers = sorted(random.sample(range(1, 50), 6))
    # Veritabanına kaydetme
    LottoDraw.objects.create(numbers=numbers)
    return Response({'numbers': numbers})

def calculate_most_common():
    all_numbers = LottoDraw.objects.values_list('numbers', flat=True)
    flat_list = [num for draw in all_numbers for num in draw]
    if not flat_list:
        return None
    return Counter(flat_list).most_common(1)[0][0]


@api_view(['GET'])
def stats(request):
    last_24h = LottoDraw.objects.filter(
        created_at__gte=timezone.now() - timedelta(hours=24)
    ).count()
    total_draws = LottoDraw.objects.count()
    return Response({
        'last_24h': last_24h,
        'total_draws': total_draws,
        'most_common': calculate_most_common()
    })