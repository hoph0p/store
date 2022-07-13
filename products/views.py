from django.shortcuts import render


# Create your views here.
# контроллеры = views(вьюхи) = функции

def index(request):
    return render(request, 'products/index.html')
