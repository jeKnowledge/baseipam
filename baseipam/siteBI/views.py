from django.utils.translation import ugettext as _
from django.shortcuts import render
from django.http import HttpResponse
from .models import Content

content = Content.objects.all()
who_are_we = content[0]
who_are_we_desc = content[1]
about_us = content[2]
about_us_desc = content[3]
mission = content[4]
mission_desc = content[5]
vision = content[6]
vision_desc = content[7]
values = content[8]
values_desc = content[9:14]
testimonials = content[14]
testimonials_first = content[15]
testimonials_second = content[16]
mm = content[17]
mm_desc = content[18]
cm = content[19]
cm_desc = content[20]
mr = content[21]
mr_desc = content[22]
commerm = content[23]
commerm_desc = content[24]
sidecard_first = content[25]



def index(request, language):
    if (language == "pt"):
        return render(request, 'siteBI/index.html', { 'who_are_we': who_are_we, 'who_are_we_desc': who_are_we_desc})

    elif (language == "en"):
        return render(request, 'siteBI/en.html', { 'who_are_we': who_are_we, 'who_are_we_desc': who_are_we_desc})

def about(request, language):
    if (language == "pt"):
        return render(request, 'siteBI/about.html', {'about_us':about_us, 'about_us_desc':about_us_desc, 'mission':mission, 'mission_desc':mission_desc, 'vision':vision, 'vision_desc':vision_desc, 'values':values, 'values_desc':values_desc, 'testimonials':testimonials, 'testimonials_first':testimonials_first, 'testimonials_second':testimonials_second})

    elif (language == "en"):
        return render(request, 'siteBI/about-en.html', {'about_us':about_us, 'about_us_desc':about_us_desc, 'mission':mission, 'mission_desc':mission_desc, 'vision':vision, 'vision_desc':vision_desc, 'values':values, 'values_desc':values_desc, 'testimonials':testimonials, 'testimonials_first':testimonials_first, 'testimonials_second':testimonials_second})


def services(request, language):
    if (language == "pt"):
        return render(request, 'siteBI/services.html', {'mm':mm, 'mm_desc':mm_desc, 'cm':cm, 'cm_desc':cm_desc, 'mr':mr, 'mr_desc':mr_desc, 'commerm':commerm, 'commerm_desc':commerm_desc, 'sidecard_first':sidecard_first})

    elif (language == "en"):
        return render(request, 'siteBI/services-en.html', {'mm':mm, 'mm_desc':mm_desc, 'cm':cm, 'cm_desc':cm_desc, 'mr':mr, 'mr_desc':mr_desc, 'commerm':commerm, 'commerm_desc':commerm_desc, 'sidecard_first':sidecard_first})
