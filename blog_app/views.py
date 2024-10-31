from django.shortcuts import render, redirect
from .models import Topic, Note
from .forms import PostForm, NoteForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    '''Домашняя страница.'''
    return render(request, 'blog_app/index.html')

@login_required()
def posts(request):
    '''Страница со всеми постами'''
    posts = Topic.objects.filter(user=request.user).order_by('date_add')
    context = {'posts':posts}
    return render(request, 'blog_app/posts.html', context)


@login_required()
def post(request, post_id):
    '''Выводит одну запись'''
    post = Topic.objects.get(id=post_id)
    if post.user != request.user:
        return render(request, 'blog_app/error.html')
    notes = post.note_set.order_by('-date_add')
    context = {'post':post, 'notes':notes}
    return render(request, 'blog_app/post.html', context)


@login_required()
def new_post(request):
    '''Опредлеляет новую тему.'''
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('blog_app:posts')

    context = {'form':form}
    return render(request, 'blog_app/new_post.html', context)


@login_required()
def new_note(request, post_id):
    '''Добавляет новую запись по конкретной теме.'''
    post = Topic.objects.get(id=post_id)
    if post.user != request.user:
        return render(request, 'blog_app/error.html')
    if request.method != 'POST':
        # Данные не отправлялись. Создаётся пустая форма
        form = NoteForm()
    else:
        # Отправлены данные POST. Обработать данные.
        form = NoteForm(data=request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.post = post
            new_note.save()
            return redirect('blog_app:post', post_id=post_id)
    # Вывести пустую или недействительную форму.
    context = {'post':post, 'form':form}
    return render(request, 'blog_app/new_note.html', context)

@login_required()
def edit_post(request, post_id):
    '''Редактирует существующую тему.'''
    # функция не используется
    post = Topic.objects.get(id=post_id)
    if post.user != request.user:
        return render(request, 'blog_app/error.html')
    if request.method != 'POST':
        # Исходный запрос. Форма заполняется данными текущей записи.
        form = PostForm(instance=post)
    else:
        # Отправка данных POST. Обработать данные.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:post', post_id=post.id)
    context = {'post':post, 'form':form}
    return render(request, 'blog_app/edit_post.html', context)



@login_required()
def edit_note(request, note_id):
    '''Редактирует существующую запись.'''
    note = Note.objects.get(id=note_id)
    post = note.post
    if request.method != 'POST':
        # Исходный запрос. Форма заполняется данными текущей записи.
        form = NoteForm(instance=note)
    else:
        # Отправка данных POST. Обработать данные.
        form = NoteForm(instance=note, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:post', post_id=post.id)
    context = {'note':note, 'post':post, 'form':form}
    return render(request, 'blog_app/edit_note.html', context)


def error(request):
    return render(request, 'blog_app/error.html')
