from django.shortcuts import render
from django.contrib.auth import login, authenticate,logout  
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,loginform,blogForm
from django.shortcuts import render, redirect
from .models import blog
from django.contrib.auth.models import User
import random

@login_required(login_url='login')
def home_view(request):
    blogs=blog.objects.filter(status='public')
    return render(request, 'home.html',{'blog':blogs})
    

def signup_view(request):
    fno=random.randint(1,9)
    sno=random.randint(1,9)

    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
        else:
            print(form.cleaned_data)
            # form = SignUpForm(request.POST,initial={'fno':str(fno),'sno':sno})
            form.data={'fno':fno,'sno':sno}
            # form.cleaned_data={**form.cleaned_data,'fno':fno,'sno':sno}
            print(form.cleaned_data)
            # print(form)
            print(form.__dict__)
            return render(request, 'signupform.html', {'form': form, 'fno':fno,'sno':sno})
            # form = SignUpForm({'fno':fno,'sno':sno})
    else:
        
        form = SignUpForm(initial={'fno':fno,'sno':sno})
        # print(form.__dict__)
    return render(request, 'signupform.html', {'form': form,'fno':fno,'sno':sno})


def login_view(request):
    if request.method=='POST':
        form=loginform(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                massege='password not matched'
                return render(request,'login.html',{'form':form,'massege':massege})   
        else:
            return render(request,'login.html',{'form':form})
    form=loginform()
    return render(request,'login.html',{'form':form})


@login_required(login_url='login')
def logout_view(request):
    
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def myBlogs_view(request):
    blogs=blog.objects.filter(author=request.user)
    return render(request, 'myblog.html',{'blog':blogs})

@login_required(login_url='login')
def create_blog(request):
    if request.method=='POST':
        form = blogForm(request.POST or None, request.FILES or None) 
        print(request.user.__dict__)

        if form.is_valid(): 
            print(request.user,'uae')
            form=form.save(commit=False)
            user=User.objects.get(username=request.user.username)
            form.author = request.user
            
            form.save() 
        else:
            return render(request,'create_blog.html',{'form':form})
    form = blogForm()
    return render(request,'create_blog.html',{'form':form})


@login_required(login_url='login')
def single_blog(request,id):
    sblog=blog.objects.get(id=id)
    return render(request,'single_blog.html',{'blog':sblog})


@login_required(login_url='login')
def search_blog(request):
    if request.method=='POST':
        username=request.POST.get('search')
        try:
            author=User.objects.get(username=username)
            blogs=blog.objects.filter(author=author,status='public')
            return render(request,'search.html',{'blog':blogs,'author':author})
        except:
            return render(request,'search.html',{'massege':"User '{}' doesn't exist".format(username)})
    return render(request,'search.html',{'massege':'You havent search anything'})



@login_required(login_url='login')
def delete_blog(request,id):
    blog.objects.filter(id=id).delete()
    return redirect('home')


@login_required(login_url='login')
def update_blog(request,id):
    
        instance=blog.objects.get(id=id)
    # if request.method=='POST':
        form = blogForm(request.POST or None, request.FILES or None,instance=instance) 
        # print(request.user.__dict__)

        if form.is_valid(): 
            
            form=form.save(commit=False)
            user=User.objects.get(username=request.user.username)
            form.author = request.user
            
            form.save() 
            return redirect('home')
        else:
            return render(request,'create_blog.html',{'form':form})
    
    # form = blogForm(instance=instance)
    # return render(request,'create_blog.html',{'form':form})