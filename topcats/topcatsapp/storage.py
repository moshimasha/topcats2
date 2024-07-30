from django.conf import settings
from django.core.files.storage import Storage
from supabase import create_client, Client




class MyStorage(Storage):
    def __init__(self, option=None):
        if not option:
            option = settings.CUSTOM_STORAGE_OPTIONS
