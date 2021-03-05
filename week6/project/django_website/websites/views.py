from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
        return HttpResponse("This is my first webpage in Python and Django! Python is a popular general-purpose programming language that can be used for a wide variety of applications. It includes high-level data structures, dynamic typing, dynamic binding, and many more features that make it as useful for complex application development as it is for scripting or glue code that connects components together. It can also be extended to make system calls to almost all operating systems and to run code written in C or C++. Due to its ubiquity and ability to run on nearly every system architecture, Python is a universal language found in a variety of different applications.")

# Create your views here.
