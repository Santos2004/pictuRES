import requests
from django.db import models
from PIL import Image
import sys
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile


class Picture(models.Model):
    name = models.CharField(max_length=100, null=True)
    url = models.URLField(null=True, blank=True, verbose_name='URL')
    picture = models.ImageField(upload_to='site_media/', null=True, blank=True)
    width = models.PositiveIntegerField(null=True, blank=True)
    height = models.PositiveIntegerField(null=True, blank=True)
    parent_picture = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='parents')

    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.picture.name
        sizes = Image.open(self.picture)
        self.width = sizes.size[0]
        self.height = sizes.size[1]
        super(Picture, self).save()

    @staticmethod
    def save_img_from_url(url):
        response = requests.get(url, stream=True).raw
        image = Image.open(response)
        file_name = url.split('/')[-1].split('.')[0]
        file_format = image.format.lower()
        output = BytesIO()
        image.save(output, format=file_format, quality=100)
        output.seek(0)
        full_file_name = f'{file_name}.{file_format}'
        picture = InMemoryUploadedFile(
            output, 'ImageField', full_file_name,
            f'media/{file_format}', sys.getsizeof(output), None
        )
        return picture

    @staticmethod
    def resize_image(image, width, height):
        if width is None:
            width = image.width
            image_name = f'{image.name}_{height}'
        elif height is None:
            height = image.height
            image_name = f'{image.name}_{width}'
        else:
            image_name = f'{image.name}_{width}_{height}'
        source_image = Image.open(image.picture)
        output = BytesIO()
        image_format = source_image.format.lower()
        new_image_size = (width, height)
        resized_image = source_image
        resized_image.thumbnail(new_image_size)
        resized_image.save(output, format=image_format, quality=100)
        output.seek(0)
        new_image_file = InMemoryUploadedFile(
            output, 'ImageField', f'{image_name}.{image_format}',
            f'media/{image_format}', sys.getsizeof(output), None
        )
        return new_image_file, image_name

    def __str__(self):
        return self.name
