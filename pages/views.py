from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from .models import Employee
from .models import Study

# Create your views here.
def index(request):
    return render(request, "index.html", {"employees": Employee.objects.all()})

# def home(request):
#     return render(request, 'index.html')

# views for search function in the homepage.


# views for goto browse page from the sidebar.
def browse(request):
    return render(request, 'browse.html', {"studies": Study.objects.all()})

def browse_results(request):
    if request.method == 'POST':
        item_name = request.POST.get('item_name')

        # 在这里执行根据请求数据查询数据库的操作
        # ...

        # 假设查询结果是一个字典
        result = {
            'item_name': item_name,
            'data': '查询的结果数据',
        }
        #return JsonResponse(result)
    return render(request, "browse_results.html")

# views for goto search page from the sidebar.
def search(request):
    return render(request, 'search.html')

# views for goto help page from the sidebar.
def help(request):
    return render(request, 'help.html')