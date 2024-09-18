from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    # request.method is GET, POST ...; request.POST is Dict {}
    if request.method=='POST': 
        form = UserCreationForm(request.POST)
        # 如果username password 是可被驗證的就存檔，返回 posts App name url 'list'
        if form.is_valid():
            login(request, form.save()) # form.save() return user
            return redirect("posts:list") 
    # else means http method: GET
    else: 
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user()) 
            if 'next' in request.POST:
                return redirect(request.POST.get('next')) # 去任何被發送的地方
            else:
                return redirect("posts:list")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("posts:list")
    