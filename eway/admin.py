from django.contrib import admin
from django.db.models import get_model

admin.site.register(get_model('eway', 'EwayTransaction'))
admin.site.register(get_model('eway', 'EwayResponseCode'))
