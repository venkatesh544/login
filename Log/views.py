from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core import paginator
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from Author.forms import NewUserForm
from Log.forms import SignUpForm
from Log.models import BDAdata, Account, Book
#paginator step
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from .forms import BooksForm

def home(request):
    return render (request,'homepage.html')


def Loginpage(request):
    if request.method == 'POST':
        if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.info(request, f"You are now logged in as {username}.")
                    return redirect("Dashboard")
                else:
                    messages.error(request, "Invalid username or password.")
            else:
                messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="Loginpage.html", context={"login_form": form})

def ABDAloginpage(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("loginpage")
            messages.error(request, "Unsuccessful registration. Invalid information.")

            form = NewUserForm()
        return render(request=request, template_name="ABDAloginpage.html", context={"register_form": form})

    return render(request,"ABDAloginpage.html")

def DDashboard(request):
    data = Account.objects.all()
    context = {'data': data}
    for i in data:
        print(i.id,i.email,i.username)
    return render(request,'Dashboard.html',context)



def Upload(request):
    if request.method == 'POST':
        form =BooksForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Books')
    else:
        form = BooksForm
    return render (request,'upload.html',{'form':form})



def BBooks(request,entries_per_page = 3):
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
    return render (request,'Book.html',context)



def Delete(request,pk):
    if request.method =='POST':
        book =Book.objects.get(pk=pk)
        book.delete()
    return redirect('Books')




