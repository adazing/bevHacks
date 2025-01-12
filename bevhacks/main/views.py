from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import *
import json
# Create your views here.

def search(request):
    institution_lists = Institution.objects.all()
    
    results = dict()
    for i in institution_lists:
        results[i.name] = "http://127.0.0.1:8000/profile/"+str(i.id)+"/"
    results = json.dumps(results)
    # print)
    # if query:
    #     results = Institution.objects.filter(
    #         Q(name__icontains=query)
    #     )
    return render(request, 'main/search.html', context={"results": results})

def profile(request, pk):
    institution = get_object_or_404(Institution, id=pk)
    if institution.admission_rate:
        institution.admission_rate *= 100
    else:
        institution.admission_rate = "No rate recorded"
    if not institution.address:
        institution.address = "Not specified"
    if not institution.home_page:
        institution.home_page = "Not specified"
    if not institution.tuition_fee_in:
        institution.tuition_fee_in = "No tuition specified"
    if not institution.tuition_fee_out:
        institution.tuition_fee_out = "No tuition specified"
    if not institution.np_curl:
        institution.np_curl = "Not specified"
    is_ethnicity_data = True
    if not (institution.men and institution.women and institution.white and institution.black and institution.hispanic and institution.asian and institution.ai_an and institution.na_pi and institution.two and institution.alien and institution.unknown):
        is_ethnicity_data=False

    # institution.control = 
    print(institution.__dict__)
    return render(request, "main/profile.html", context={"institution":institution, "is_ethnicity_data": is_ethnicity_data})

def home(request):
    return render(request, "main/home.html")

def about(request):
    return render(request, "main/about.html")