import requests
import plotly.express as px
from django.shortcuts import render
import pandas as pd

REQUEST_BASE = "https://api.data.gov/ed/collegescorecard/v1/schools?api_key=OQlFQaitCa3V9XZMRyUUhJOfSmuE0yagABGDgkXF"
all_schools = []



# for i in range(65):
#     contents =requests.get(f"{REQUEST_BASE}&fields=school.name&page={i}&per_page=100&sort=school.name:asc")

#     if contents.status_code == 200:
#         data = contents.json()
#         school_names = [item['school.name'] for item in data["results"]]
#         all_schools+=school_names

#     else:
#         print(f"{i} : Error: {contents.status_code}")
# print(all_schools)

contents =requests.get(f"{REQUEST_BASE}&page=1&per_page=100&fields=school.name")
data = ""
if contents.status_code == 200:
    data = contents.json()
print(data)
# with open("all_colleges.out", "w") as f:
#     for school in all_schools:
#         f.write(school+"\n")




def my_view(request):
    # Fetch data from your Django models
    data = ...

    # Create a Plotly figure
    fig = px.bar(data, x="category", y="value")

    # Convert the figure to HTML
    plot_div = fig.to_html(full_html=False)

    # Pass the plot to your template
    context = {"plot_div": plot_div}
    return render(request, "my_template.html", context)#TODO:change template name


#general
    #ADM_RATE_ALL (admission rates)
    #CONTROL(type of school: public, private, etc)(we have to convert 1,2,3 to their corresponding values)
    #ADDR,  CITY, STABBR,  ZIP
    #LATITUDE, LONGITUDE
    #INSTURL(homepage for school)

#test scores/stats
    #SATVR{25,50,75} (reading)
    #SATMT{25,50,75} (math)


#Paying for stuff
    #TUITIONFEEIN(in state)
    #TUITIONFEEOUT(out of state)
    #NPCURL(price claculator for that school!!)

#diversity
    # men (UGDS_MEN)
    # women (UGDS_WOMEN)
    # white (UGDS_WHITE)
    # black (UGDS_BLACK)
    # Hispanic (UGDS_HISP)
    # Asian (UGDS_ASIAN)
    # American Indian/Alaska Native (UGDS_AIAN)
    # Native Hawaiian/Pacific Islander (UGDS_NHPI)
    # two or more races (UGDS_2MOR)
    # non-resident aliens (UGDS_NRA)
    # race unknown (UGDS_UNKN)

#TODO: USE GUAGE CHARTS