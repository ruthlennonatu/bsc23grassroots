from django.shortcuts import render, redirect
from .forms import PersonForm


def create_person(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect()  # todo create a view for when the form is saved
    else:
        form = PersonForm()
    return render(request, 'Source/grassroots/templates/form.html', {'form': form})
