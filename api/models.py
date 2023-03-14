from django.db import models


# Create a Contact table
class Contact(models.Model):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.address

# Create a Student table
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=20)
    contact = models.OneToOneField(Contact,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.last_name} {self.first_name}'
    




