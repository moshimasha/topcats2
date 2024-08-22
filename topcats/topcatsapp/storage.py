from django.conf import settings
from django.core.files.storage import Storage
from supabase import create_client, Client
from storage3.utils import StorageException
import io
from io import BytesIO


class FileStorage(Storage):
    def __init__(self):
        self.supabase: Client = create_client(settings.AWS_S3_ENDPOINT_URL, settings.SUPABASE_ANON_KEY)
        self.bucket_name = settings.SUPABASE_BUCKET_NAME   
    def listall(self):
        userpath = self.supabase.auth.get_session().user.id
        folder_path = userpath + "/"
        data = self.supabase.storage.from_(settings.SUPABASE_BUCKET_NAME).list(path=folder_path)   
        return data                                
    def _open(self, name, mode='rb' ):
       userpath = self.supabase.auth.get_session().user.id + "/"
       response =  self.supabase.storage.from_(self.bucket_name).download(userpath + name)
       reserve_pdf_on_memory = io.BytesIO(response)
       return reserve_pdf_on_memory
    def _save(self, name, content):
        file_content = content.read()
        userpath = self.supabase.auth.get_session().user.id
        self.supabase.storage.from_(self.bucket_name).upload(userpath + "/" + name, file_content, file_options={"content-type":"application/pdf"})
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

