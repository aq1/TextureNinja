from django.contrib import admin

import textureDB

admin.site.register(textureDB.models.Texture)
admin.site.register(textureDB.models.RealImage)
admin.site.register(textureDB.models.RenderedImage)
