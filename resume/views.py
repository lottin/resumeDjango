# from django.shortcuts import render
# from .models import Education, Interest, ContactInfo, Contact, Profile, Language, Experience, Skill
# # Create your views here.
# def index(request):
#     contact_infos = ContactInfo.objects.all()
#     interests = Interest.objects.all()
#     educations = Education.objects.all()
#     profiles = Profile.objects.all()
#     languages = Language.objects.all()
#     experiences = Experience.objects.all()
#     skills = Skill.objects.all()

#     return render(request, 'resume/index.html', {
#         'contact_infos':contact_infos,
#         'interests':interests,
#         'educations':educations,
#         'profiles':profiles
#     })