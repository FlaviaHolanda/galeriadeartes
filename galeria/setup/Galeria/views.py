from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ImageForm, CommentForm
from .models import Image, Comment

# Create your views here.


def cadastrar(request):
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username =form.cleaned_data.get("username")
            messages.success(request, f"Conta cadastrada para {username}")
            
    else:
        form = UserCreationForm()
    return render(request, 'Galeria/cadastro.html', {"form": form})


    


#def cadastro(request):
    #if request.method == "GET":
    #    return render(request, 'Galeria/cadastro.html')
    #else:
    #    username = request.POST.get("username")
    #    password = request.POST.get("password")

    #    user = User.objects.get(username=username, password=password)

     #   if user:
    #        return HttpResponse("usuario ja existe")
        
    #user = User.objects.create_user(username= username, password= password)
   # user.save()

    #return HttpResponse("usuario cadastrado com sucesso") 

def Login(request):

    
    if request.method == "POST":    
        username=request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            

            return redirect('inicio/list')
        
        else :
            messages.error(request,"Usuario ou Senha invalido")

    return render(request, "Galeria/login.html")

    
        
def inicio(request):
    images = Image.objects.all()
    return render(request, "Galeria/inicio.html", {'images': images})
    
        

def image_upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
    else:
        form = ImageForm()
    return render(request, "Galeria/image_upload.html",{'form': form})
    
def image_list(request):
    context = {'image': Image.objects.all()}
    return redirect('inicio', context)



def image_detail(request, pk):
    image = Image.objects.get(pk=pk)
    comments = image.comments.all()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.image = image
            new_comment.save()
            return redirect("image_detail", pk=image.pk )
    else:
        comment_form= CommentForm()

    return render(request, 'Galeria/image_detail.html', {
        "image": image,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
        })






def addcomment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            data = Comment()
            data.name = form.cleaned_data["name"]
            data.comment = form.cleaned_data["comment"]
            form.save()
            return render(request, "inicio", {"comment": Comment.objects.all()})
        


    

