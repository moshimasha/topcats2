from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from attrs import define

@define
class GoogleLoginCredentials:
    client_id: str
    client_secret: str
    project_id: str

def google_login_get_credentials() -> GoogleLoginCredentials:
    client_id = settings.GOOGLE_OAUTH2_CLIENT_ID
    client_secret = settings.GOOGLE_OAUTH2_CLIENT_SECRET
    project_id = settings.GOOGLE_OAUTH_PROJECT_ID
    
    if not client_id:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_CLIENT_ID missing.")
    if not client_secret:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_CLIENT_SECRET missing.")
    if not project_id:
        raise ImproperlyConfigured("GOOGLE_OAUTH2_CLIENT_SECRET missing.")
    credentials = GoogleLoginCredentials(client_id = client_id, client_secret=client_secret, project_id=project_id)
    return credentials