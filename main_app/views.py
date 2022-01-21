from django.shortcuts import render
from django.views.generic.edit import CreateView
from .forms import WidgetForm
from main_app.models import Widget

# Create your views here.
def home(request):
    widgets = Widget.objects.all()
    widget_form = WidgetForm()
    return render(request,'index.html', {
        'widgets': widgets,
        'widget_form': widget_form,
    })

class WidgetCreate(CreateView):
    model = Widget
    fields = '__all__'

    success_url = '/'

     