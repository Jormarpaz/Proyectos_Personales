from django.shortcuts import render, redirect
from django.urls import reverse
from django import forms

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry_content = util.get_entry(title)
    if entry_content is None:
        return render(request, "encyclopedia/error.html", {
            "error": "Your requested page was not found."
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": entry_content
        })
    
def search(request):
    query = request.GET.get('q', '')
    if util.get_entry(query):
        return redirect(reverse('entry', args=[query]))
    else:
        entries = [entry for entry in util.list_entries() if query.lower() in entry.lower()]
        return render(request, 'encyclopedia/search.html', {
            'query': query,
            'entries': entries
        })
    
class NewPageForm(forms.Form):
    title = forms.CharField(label="Title", widget=forms.TextInput())
    content = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write the entry using Markdown', 'style': 'height: 200px;'}), label="")

def create(request):
    if request.method == "POST":
        form = NewPageForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            if util.get_entry(title):
                return render(request, "encyclopedia/create.html", {
                    "form": form,
                    "error": "An entry with this title already exists."
                })
            else:
                util.save_entry(title, content)
                return redirect(reverse("entry", args=[title]))
    else:
        form = NewPageForm()
    return render(request, "encyclopedia/create.html", {
        "form": form
    })

