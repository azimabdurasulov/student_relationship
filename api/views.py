from django.shortcuts import render
from .models import Student,Contact
from django.http import JsonResponse,HttpRequest

# Create view for Student
def get_student(request:HttpRequest)->JsonResponse:
    """
    Get all student
    """
    students=Student.objects.all()
    contacts=Contact.objects.all()
    result={}
    for student in students:
        result[student.id]={
            'first_name': student.first_name,
            'last_name':student.last_name,
            'number':student.contact.phone,
            'address':student.contact.address
            }
        
    # for contact in contacts:
    #     result[student.id]['number']=contact.phone
    #     result[student.id]['adress']=contact.address
        
    return JsonResponse(result)



