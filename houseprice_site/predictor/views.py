from django.shortcuts import render
from .ml_model import predict_price


def home(request):
    price = None

    if request.method == "POST":
        area = int(request.POST['area'])
        bedrooms = int(request.POST['bedrooms'])
        bathrooms = int(request.POST['bathrooms'])
        age = int(request.POST['age'])

        price = predict_price(area, bedrooms, bathrooms, age)

    return render(request, 'index.html', {'price': price})
