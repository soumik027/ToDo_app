from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Task
# Create your views here.

# Helper function to get or create session key
def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

# Home page - list tasks for this session only
def home(request):
    session_key = get_session_key(request)
    tasks = Task.objects.filter(session_key=session_key)

    if request.method == "POST":
        task_text = request.POST.get('task')
        if task_text:
            Task.objects.create(task=task_text, session_key=session_key)
        return redirect('home')

    context = {'tasks': tasks}
    return render(request, 'home.html', context)

# add tasks
def addTask(request):
    task=(request.POST['task'])
    Task.objects.create(task=task)
    return redirect('home')

# mark as done
def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=True
    task.save()
    return redirect('home')

# mark as undo
def mark_as_undo(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed=False
    task.save()
    return redirect('home')

# edit task
def edit_task(request,pk):
    get_task = get_object_or_404(Task,pk=pk)
    if request.method=='POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context={
            'get_task':get_task,
        }
        return render(request,'edit_task.html',context)
    
# delete task
def delete_task(request, pk):  # <-- It must be pk!
    task = get_object_or_404(Task, id=pk)
    task.delete()
    return redirect('home')

