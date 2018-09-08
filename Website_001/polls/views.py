from django.http import HttpResponse


def index(request):
    return HttpResponse("<body background=\"https://png.pngtree.com/element_pic/16/05/24/0057432e09b9f62.jpg\"><h2 style=\"background-color:Cyan;\"><center>Welcome to Django & Python First page</center></h2></body></html>")
