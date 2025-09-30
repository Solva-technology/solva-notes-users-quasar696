from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Note
from django.contrib.auth.models import User
from .forms import NoteForm


def note_list(request):
    template_name = 'note_list.html'
    notes = Note.objects.select_related(
        "author", "status"
    ).prefetch_related("categories").order_by("-created_at")
    context = {'notes': notes}
    return render(request, template_name, context)


def note_detail(request, note_id):
    template_name = 'note_detail.html'
    note = get_object_or_404(Note, id=note_id)
    context = {'note': note}
    return render(request, template_name, context)


def user_detail(request, user_id):
    template_name = "user_detail.html"
    user = get_object_or_404(User, id=user_id)
    notes = user.note_set.select_related("status").all()
    context = {
        "user": user,
        "notes": notes
    }
    return render(request, template_name, context)


@login_required
def note_create(request):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            form.save_m2m()
            return redirect("notes:note_list")
    else:
        form = NoteForm()
    return render(request, "note_form.html", {"form": form, "title": "Создать заметку"})


@login_required
def note_edit(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if not (request.user == note.author or request.user.is_staff):
        raise PermissionDenied("Доступ запрещен")
    if request.method == "POST":
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect("notes:detail", note_id=note.id)
    else:
        form = NoteForm(instance=note)
    return render(request, "note_form.html", {"form": form, "title": "Редактировать заметку"})


@login_required
def note_delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if not (request.user == note.author or request.user.is_staff):
        raise PermissionDenied("Доступ запрещен")
    if request.method == "POST":
        note.delete()
        return redirect("notes:note_list")
    return render(request, "note_confirm_delete.html", {"note": note})
