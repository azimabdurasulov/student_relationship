from django.shortcuts import render
from .models import Student,Contact
from django.http import JsonResponse,HttpRequest

# Create view for Student
def get_student(request:HttpRequest)->JsonResponse:
    """
    Get all student
    """
    pass


