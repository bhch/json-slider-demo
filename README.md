# JSON Slider Demo

This app implements an image slider using `JSONField`.

It uses [django-jsonform][django-jsonform] to create a dynamic, user-friendly
form for editing JSON.

A `JSONField` yields better performance than `ForeignKey` when querying
is not required. An image slider is a perfect use case of this (see [supplementary blog post][blog] for more).

This app exists to showcase some of the features of [django-jsonform][django-jsonform].
As such, consider modifying this app as per your needs.

## Demo

[![Play video][video-thumbnail]][video]

## Install

**0. Note:**

It is assumed that you already have a Django project set up ([with media serving enabled][serve-media]).

**1. Clone or [download][download-repo] this repo.**

Then copy the `sliderapp` folder into your Django project.

**2. Install [django-jsonform][django-jsonform]:**

This dependency is required for creating a user-friendly JSON editing form in the admin.

```sh
pip install -U django-jsonform
```

**3. Update settings**

```python
# settings.py

INSTALLED_APPS = [
    ...
    'django_jsonform',
    'sliderapp',
]
```

**4. Include URLs**

```python
# project/urls.py

urlpatterns = [
    ...
    path('sliderapp/', include('sliderapp.urls')),
]
```

**5. Apply migrations**

```sh
python manage.py migrate
```

## Usage

 1. Go to the admin page and [create a slider][create-slider].
 2. Open http://127.0.0.1:8000/sliderapp/demo/ to view the slider.

## License

This repo is available under [Public Domain license][license].

[django-jsonform]: https://github.com/bhch/django-jsonform
[serve-media]: https://docs.djangoproject.com/en/4.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
[download-repo]: https://github.com/bhch/json-slider-demo/archive/refs/heads/master.zip
[video-thumbnail]: screenshots/video-thumbnail.png?v=3
[video]: https://github.com/bhch/json-slider-demo/issues/1
[create-slider]: http://127.0.0.1:8000/admin/sliderapp/slider/add/
[view-slider]: http://127.0.0.1:8000/sliderapp/demo/
[blog]: https://bhch.github.io/posts/2022/09/creating-an-image-slider-in-django-using-json/
[license]: LICENSE.txt
