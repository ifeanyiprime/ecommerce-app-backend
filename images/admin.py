from django.contrib import admin

from .models import Image


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "image_file",
        "product",
        "thumbnail",
        "main",
    )


admin.site.register(Image, ImageAdmin)
