from django.shortcuts import render
from .models import Feature, Slider
from django.db.models import Q, query
from django.shortcuts import redirect

# def feature(request):
#     features = Feature.objects.all()[:3]

#     context = {
#         'features':features,
#     }
#     return render(request, 'carousel/index.html', context)


def slider(request):
    sliders = Slider.objects.all()
    features = Feature.objects.all()[:3]

    context = {
        'features': features,
        'sliders': sliders
    }
    return render(request, 'carousel/index.html', context)
