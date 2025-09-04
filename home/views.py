from django.shortcuts import render
from .models import *
import time
import random

def home(request):
        
         
    return render(request , 'index.html' )