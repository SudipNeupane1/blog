
# from django.contrib.auth import authenticate,login,get_user_model
# from .forms import ContactForm 
import random
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from articles.models import Article
# def home(request,*args, **kwargs):
#     context ={
#         "title":"hello world",
#         "content":"welcome to the page",
        
#     }
#     return render(request,'home.html',context)



# def about(request):
#     context = {
#         "title":"Abount Page",
#         "content":"Welcome to the about page."
#     }
#     return render(request,"about.html",context)


# def contact(request):
#     contact_form + ContactForm(request.POST or NOne)
#     context = { 
#         "title": "Contact page",
#         "context":"Welcome to the contact",
#         "form"  : "contact_form",      
#         }

#     }
#     if contact_form.is_valid():
#         # print(contact_form.cleaned_data)
#     return render(request,"contact/view.html".context)


def home(request,*args,**kwargs):
    name = "Sudip"
    random_id = random.randint(1,4)


    # from database
    article_obj = Article.objects.all().first()
    article_queryset =Article.objects.all()
    context = { 
        "object_list":article_queryset,
        "object":article_obj
    }
    HTML_STRING = render_to_string("home.html", context=context)
    return HttpResponse(HTML_STRING)