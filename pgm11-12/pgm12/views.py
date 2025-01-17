from django.shortcuts import render, redirect
from django.http import JsonResponse 
from .forms import StudentForm
def student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST) 
        if form.is_valid():
            student = form.save()
            return JsonResponse({'success': True})
    else:
        form = StudentForm()
    return render(request, 'register_student.html', {'form': form})