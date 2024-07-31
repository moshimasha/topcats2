from django.conf import settings
from django.core.files.storage import Storage
from supabase import create_client, Client
from storage3.utils import StorageException
from io import BytesIO




class FileStorage(Storage):
    def __init__(self):
        self.supabase: Client = create_client(settings.AWS_S3_ENDPOINT_URL, settings.SUPABASE_ANON_KEY)
        self.bucket_name = settings.SUPABASE_BUCKET_NAME                                      
    def _open(self, name, mode='rb'):
       response =  self.supabase.storage.from_(self.bucket_name).download(name)
       file_obj = BytesIO(response)
       return file_obj
    def _save(self, name, content):
        print(type(name))
        print(type(content))
        file_content = content.read()
        response = self.supabase.storage.from_(self.bucket_name).upload(name, file_content, file_options={"content-type":"application/pdf"})
        return response.json()
    def delete(self, name):
        response = self.supabase.storage.from_(self.bucket_name).remove([name])
    def url(self, name):
        return self.supabase.storage.from_(self.bucket_name).list()
    def exists(self, name):
        try: 
            response = self.supabase.storage.from_(
                self.bucket_name).list(path=name)
            return len(response)>0
        except StorageException:
            return False

