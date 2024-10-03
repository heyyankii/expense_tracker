from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ExpenseForm
from .models import Expense
from django.db.models import Sum
from django.utils import timezone
from datetime import datetime

def home(request):
    return render(request, 'expenses/home.html')

def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('add_expense')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})

def summary_by_date(request):
    expenses = None
    total = 0
    date_query = None
    if request.method == 'POST':
        date_str = request.POST.get('date')
        try:
            date_query = datetime.strptime(date_str, '%Y-%m-%d').date()
            expenses = Expense.objects.filter(date=date_query)
            total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
        except ValueError:
            messages.error(request, 'Invalid date format. Please use YYYY-MM-DD.')
    return render(request, 'expenses/summary_by_date.html', {
        'expenses': expenses,
        'total': total,
        'date': date_query,
    })

def summary_by_category(request):
    expenses = None
    total = 0
    category = None
    if request.method == 'POST':
        category = request.POST.get('category')
        if category not in dict(Expense.CATEGORY_CHOICES):
            messages.error(request, 'Invalid category selected.')
        else:
            expenses = Expense.objects.filter(category=category)
            total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'expenses/summary_by_category.html', {
        'expenses': expenses,
        'total': total,
        'category': category,
        'categories': dict(Expense.CATEGORY_CHOICES).keys(),
    })