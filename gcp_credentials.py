
from google.oauth2 import service_account
#import secret_env # Uncomment this for local debugging. Must come BEFORE import constants.
import constants



# A module to return the GCP credentials.


# Return an Oauth2 credentials instance
def get_credentials(with_keyfile=False):
    keyfile_dict = _get_keyfile_dict()
    scope = [constants.GCP_SCOPE]
    creds = service_account.Credentials.from_service_account_info(keyfile_dict).with_scopes(scope)

    if not with_keyfile:
        return creds
    else:
        # Return creds and the keyfile.
        return creds, keyfile_dict


# Construct a dictionary of the required key:value pairs.
def _get_keyfile_dict():
    keyfile_dict = {}
    keyfile_dict['type'] = constants.GCP_TYPE
    keyfile_dict['client_email'] = constants.GCP_CLIENT_EMAIL
    keyfile_dict['private_key'] = constants.GCP_PRIVATE_KEY
    keyfile_dict['private_key_id'] = constants.GCP_PRIVATE_KEY_ID
    keyfile_dict['client_id'] = constants.GCP_CLIENT_ID
    keyfile_dict['token_uri'] = constants.GCP_TOKEN_URI
    keyfile_dict['project_id'] = constants.GCP_PROJECT_ID
    return keyfile_dict
