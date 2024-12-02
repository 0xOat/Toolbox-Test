from django.shortcuts import render
from django.views.generic import DeleteView
# Create your views here.
from django.urls import reverse_lazy
from .models import Book

class DelData(DeleteView):
    model = Book
    template_name = "del.html"
    fields = ["title","author"]
    success_url = reverse_lazy("done")

def done(req):
    return render(req, "done.html")