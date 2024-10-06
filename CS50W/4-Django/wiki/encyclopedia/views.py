from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    try:
        return render(request, "encyclopedia/entry.html", {
            "entry": util.get_entry(title)
        })
    except TypeError:
        return render(request, "encyclopedia/error.html", {
            "error": "Your requested page was not found."
        })

