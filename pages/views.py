from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    return render(request, "index.html", {"employees": Employee.objects.all()})

# views for search function in the homepage.


# views for goto browse page from the sidebar.


# views for goto search page from the sidebar.


# views for goto help page from the sidebar.