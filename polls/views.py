from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Habit, Progress
from .forms import HabitForm, CustomUserCreationForm, ProgressForm

def landing_page(request):
    return render(request, 'polls/landing_page.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'polls/register.html', {'form': form})

@login_required
def dashboard(request):
    if request.user.is_authenticated:
        # Get habits specific to the logged-in user
        habits = Habit.objects.filter(user=request.user)
        return render(request, 'polls/dashboard.html', {'habits': habits})
    else:
        return redirect('login')

@login_required
def create_habit(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user  # Associate the habit with the logged-in user
            habit.save()
            return redirect('habit_list')  # Redirect to the habit list
    else:
        form = HabitForm()
    return render(request, 'polls/create_habit.html', {'form': form})

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)  # Only show habits for the logged-in user
    return render(request, 'polls/habit_list.html', {'habits': habits})

@login_required
def update_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)
        if form.is_valid():
            form.save()
            return redirect('habit_list')
    else:
        form = HabitForm(instance=habit)
    return render(request, 'polls/update_habit.html', {'form': form})

@login_required
def delete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        habit.delete()
        return redirect('habit_list')
    return render(request, 'polls/delete_habit.html', {'habit': habit})

@login_required
def habit_progress(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    progress = Progress.objects.filter(habit=habit).order_by('-date')
    return render(request, 'polls/habit_progress.html', {'habit': habit, 'progress': progress})

@login_required
def add_progress(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id, user=request.user)
    if request.method == 'POST':
        form = ProgressForm(request.POST)
        if form.is_valid():
            progress = form.save(commit=False)
            progress.habit = habit
            progress.save()
            return redirect('habit_progress', habit_id=habit.id)
    else:
        form = ProgressForm()
    return render(request, 'polls/add_progress.html', {'habit': habit, 'form': form})