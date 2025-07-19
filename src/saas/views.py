import pathlib
from django.shortcuts import render
from django.http import HttpResponse

from visits.models import PageVisit

cwd = pathlib.Path(__file__).resolve().parent

# def home_page_view(request, *args, **kwargs):
#     """
#     A simple view that returns a welcome message.
#     """
#     return HttpResponse("<h1>Welcome to our APP!</h1>")

# def home_page_view(request, *args, **kwargs):
#     html_ = cwd.joinpath("home.html").read_text()
#     return HttpResponse(html_)

# def home_page_view(request, *args, **kwargs):
#     my_title = "My SaaS App"
#     my_context = {
#         "page_title": my_title,
#         "my_content": "This is the content of the home page.",
#     }
    
#     html_ = """
#         <!DOCTYPE html>
#         <html lang="en">
#             <body>
#                 <h1>Welcome to our {page_title}!</h1>
#             </body>
#         </html>
#     """.format(**my_context)
#     return HttpResponse(html_)

# def home_page_view(request, *args, **kwargs):
#     my_title = "My SaaS App"
#     my_context = {
#         "page_title": my_title,
#         "my_content": "This is the content of the home page.",
#     }
    
#     html_ = ""
#     html_template = "home.html"
#     return render(request, html_template, my_context)

def home_page_view(request, *args, **kwargs):
    queryset = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My SaaS App"
    my_context = {
        "page_title": my_title,
        "my_content": "This is the content of the home page.",
        "queryset": queryset,
        "page_visit_count": page_qs.count(),
        "page_visit_percentage": page_qs.count() * 100 / queryset.count() if queryset.count() > 0 else 0,
        "total_visits": queryset.count(),
    }
    
    html_template = "home.html"
    PageVisit.objects.create(path=request.path)  # Log the page visit
    return render(request, html_template, my_context)
