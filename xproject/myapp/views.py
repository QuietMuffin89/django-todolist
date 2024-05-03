from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Item
# Create your views here.
def index(request):

    item_qs = Item.objects.all()

    return render(
        request=request,
        template_name="myapp/index.html",
        context={
           "item_qs": item_qs
        }
    )