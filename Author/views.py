from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from Author.forms import NewUserForm
from Log.models import Book


def House(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username,password = password)
            if user is not None:
                login(request,user)
                messages.info(request,"You are now logged in as {username}.")
                return redirect("Ather_Books_store")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request,template_name="User_login.html",context={"login_form":form})


def AAther_Book(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("house")
            messages.error(request, "Unsuccessful registration. Invalid information.")

            form = NewUserForm()
        return render(request=request, template_name="Ather_Book.html", context={"register_form": form})


    return render(request, 'Ather_Book.html')


def AAther_Log(request):
    return render(request,'User_login.html')




def AAther_Book_store(request,entries_per_page = 3):
    ACCOUNTS_PER_PAGE = entries_per_page

    storage =Book.objects.all()
    if request.method == "GET":
        user = request.GET.get('user')

        if user:
            storage = Book.objects.all().filter(
                Q(title__icontains=user)).distinct()


        p = Paginator(storage.all(), ACCOUNTS_PER_PAGE)
        page = request.GET.get('page',1)
#       Books = paginator.page(3)
#       Books = paginator.page(paginator.num_pages)

    try:
        Books = p.get_page(page)
    except PageNotAnInteger:
        Books = p.page(ACCOUNTS_PER_PAGE)
    except EmptyPage:
        Books = p.page(p.num_pages)

    context = {
        'Books': Books,
    }
    return render (request,'AAther_Book.html',context)


def Loginpage(request):
    return render(request, 'Loginpage.html')
