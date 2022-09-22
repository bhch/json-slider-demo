from django.db import models
from django.urls import reverse_lazy
from django_jsonform.models.fields import JSONField


class Slider(models.Model):
    SLIDES_SCHEMA = {
        'type': 'list',
        'items': {
            'type': 'dict',
            'keys': {
                'image': {
                    'type': 'string',
                    'format': 'file-url',
                    'handler': reverse_lazy('sliderapp:slider-image-handler'),
                    'required': True,
                },
                'bg': {
                    'type': 'string',
                    'format': 'color',
                    'title': 'Background',
                    'default': '#ffffff',
                },
                'caption': {
                    'type': 'string',
                    'widget': 'textarea',
                },
                'button': {
                    'type': 'dict',
                    'keys': {
                        'text': {'type': 'string'},
                        'link': {'type': 'string'},
                    },
                },
            },
        },
        'minItems': 1,
    }

    name = models.CharField(max_length=50, help_text='e.g.: Landing page slider')
    slides = JSONField(schema=SLIDES_SCHEMA)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('sliderapp:demo')


class SliderImage(models.Model):
    image = models.ImageField(upload_to='sliderapp')
