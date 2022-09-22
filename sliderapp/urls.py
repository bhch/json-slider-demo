from django.urls import path
from sliderapp.views import demo, slider_image_handler


app_name = 'sliderapp'

urlpatterns = [
    path('demo/', demo, name='demo'),
    path('slider-image-handler/', slider_image_handler, name='slider-image-handler'),
]
