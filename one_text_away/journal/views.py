from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
#Created my Jibendu007
def index(request):
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        return redirect('/journal')

    return render(request, 'journal/index.html', {'todos': todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/journal',pk=pk)
