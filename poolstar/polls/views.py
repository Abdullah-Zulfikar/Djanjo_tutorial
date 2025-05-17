from django.shortcuts import render
from .models import Question, Choices

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')
