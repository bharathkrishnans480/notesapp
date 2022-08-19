from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView
from mynotes.models import Notes
from mynotes.forms import MyNotesForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.
class CreateNotesView(CreateView):
    model=Notes
    template_name = "mynotes.html"
    form_class = MyNotesForm
    success_url = "home"
    def form_valid(self, form):
        messages.success(self.request,"submission successfull")
        self.object=form.save()
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context["notes"]=Notes.objects.all().order_by("-posted_date")              #assigning a key "notes" and calling all objects from database and order_by for sorting,- for ascending order
        return context
class Notes2View(TemplateView):
    template_name = "notes.html"



class EditNotesView(View):
    model=Notes
    template_name = "mynotes.html"
    form_class = MyNotesForm
    success_url = "home"
    def get(self, request, *args, **kwargs):
        note_id = kwargs.get("post_id")
        note = Notes.objects.get(id=note_id)
        form = MyNotesForm(instance=note)
        return render(request, "edit.html", {"form": form})
    def post(self,request,*args,**kwargs):
        note_id = kwargs.get("post_id")
        note = Notes.objects.get(id=note_id)
        form=MyNotesForm(request.POST,instance=note,files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "successfully added")
            return redirect("home")
        else:
            messages.error(request, "sorry failed to add")
            return render(request, "edit.html", {"form": form})


def delete(request,*args,**kwargs):
    note=Notes.objects.get(id=kwargs.get('post_id'))
    note.delete()
    return redirect('home')