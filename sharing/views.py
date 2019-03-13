from django.shortcuts import render, redirect, HttpResponse
from sharing.forms import ChangeForm
from sharing.forms import SignUpForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
import json
from sharing.models import Share


def index(request):
    return render(request, 'index.html', {'sharings': Share.get_all()})


# Добавить организацию
@login_required
def add_powerbank_sharing(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        address = request.POST.get('address')
        crds = json.loads(request.POST.get('crds'))
        new_sharing = Share(title=title, address=address, crds_lot=crds[0], crds_lat=crds[1])
        new_sharing.save()
        return HttpResponse('Новая точка выдачи успешно добавлена!')
    context = {}
    return render(request, 'sharing/add.html', context)


# Работа с пользователем
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def account(request):
    return render(request, 'registration/account.html', {'user': request.user})

@login_required
def change(request):
    if request.method == 'POST':
        form = ChangeForm(request.user ,request.POST)
        if form.is_valid():
            current_user = form.save()
            update_session_auth_hash(request, current_user)
            current_user.save()
            return redirect('/')
    else:
        form = ChangeForm(request.user)
    return render(request, 'registration/change.html', {'form': form})

