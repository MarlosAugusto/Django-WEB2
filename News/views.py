from django.shortcuts import render, redirect
from .models import New, Comment
from .forms import NewForm

def home(request):
  news = New.objects.all()
  return render(request, 'home.html', {'news': news})

def new(request, codigo):
  form = NewForm(request.POST or None)
  new = New.objects.get(id=codigo)
  comments = Comment.objects.all().filter(news=codigo)

  if form.is_valid():
    comment = form.save(commit=False)
    print("message: ", comment)
    comment.news_id = new.id
    comment.save()
    return redirect('home')
  return render(request, 'new.html', {'form': form, 'new': new, 'comments': comments})

# def listar_news(request):
#   news = News.objects.all()
#   return render(request, 'news.html', {'news': news})
