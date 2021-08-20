# from django.db import models

# # Create your models here.
# class ContactInfo(models.Model):
#     tel = models.CharField( max_length=50)
#     linkedIn_url = models.CharField( max_length=50)
#     email = models.EmailField( max_length=254)
#     location = models.CharField(max_length=50)

#     def __str__(self):
#         return self.email

# class Education(models.Model):
#     start_year= models.DateTimeField(auto_now=True)
#     end_year = models.DateTimeField( auto_now=True)
#     school = models.CharField(max_length=50)
#     certificate = models.CharField(max_length=50)

#     def __str__(self):
#         return self.certificate
    
    
# class Language(models.Model):
#     name = models.CharField(max_length=100)
#     percentage_accuracy = models.IntegerField()

#     def __str__(self):
#         return self.name
    

# class Profile(models.Model):
#     about = models.TextField()

# class Experience(models.Model):
#     role = models.CharField(max_length=50)
#     job_desription = models.CharField(max_length=50)
#     start_date = models.DateTimeField(auto_now=True)
#     end_date =models.DateTimeField( auto_now=True)
#     company = models.CharField( max_length=50)

#     def __str__(self):
#         return self.role

# class Skill(models.Model):
#     name = models.CharField( max_length=50)
#     percentage = models.IntegerField(range(100))

#     def __str__(self):
#         return self.name
    

# class Interest(models.Model):
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.name

# class Contact(models.Model):
#     name = models.CharField( max_length=50)
#     email = models.EmailField()
#     tel = models.CharField(max_length=100)
#     content = models.TextField()

#     def __str__(self):
#         return self.name
    