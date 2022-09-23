from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from sliderapp.models import Slider, SliderImage


def demo(request):
    """View for demo page."""

    sliders = Slider.objects.all()
    return render(request, 'sliderapp/demo.html', {'sliders': sliders})


@login_required
def slider_image_handler(request):
    """View for handling AJAX file uploads in admin.
    
    See: https://django-jsonform.rtfd.io/en/latest/guide/upload.html#handling-file-uploads
    """

    if request.method == 'POST':
        image = request.FILES['file']
        img = SliderImage.objects.create(image=image)
        return JsonResponse({'value': img.image.name})

    elif request.method == 'GET':
        page = int(request.GET.get('page', 1))

        imgs_per_page = 10

        start = (page - 1) * imgs_per_page
        end = start + imgs_per_page

        results = []

        for img in SliderImage.objects.all().order_by('-pk')[start:end]:
            results.append({
                'value': img.image.name,
                'thumbnail': img.image.url,
                'metadata': {
                     'name': img.image.name.split('/')[-1],
                     'size': '%s KB' % (img.image.size / 1000),
                }
            })

        return JsonResponse({'results': results})

    elif request.method == 'DELETE':
        trigger = request.GET.get('trigger')
        file_names = request.GET.getlist('value')

        if trigger != 'delete_button':
            # if deletion is not triggered by Delete button,
            # exit the view
            return HttpResponse(status=200)

        for name in file_names:
            try:
                img = SliderImage.objects.get(image=name)
            except SliderImage.DoesNotExist:
                # :TODO: log error
                continue
            else:
                img.delete()

        return HttpResponse(status=200)
