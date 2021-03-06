client_key="System-wide: Ubuntu (wadlwalker)"
request_token_url='https://launchpad.net/+request-token'
base_authorization_url = 'https://launchpad.net/+authorize-token'
access_token_url = 'https://launchpad.net/+access-token'
import oauthlib
import requests
from requests_oauthlib import OAuth1Session
oauth = OAuth1Session(client_key, signature_method=oauthlib.oauth1.SIGNATURE_PLAINTEXT, signature_type='body')
fetch_response = oauth.fetch_request_token(request_token_url)
resource_owner_key = fetch_response.get('oauth_token')
resource_owner_secret = fetch_response.get('oauth_token_secret')
authorization_url = oauth.authorization_url(base_authorization_url) +'&allow_permission=DESKTOP_INTEGRATION'
print('Please go here and authorize,', authorization_url)
input('Press enter, when done.')
# Step 1: use signature_type='body'
# Step 2: no verifier set
# Step 3: set Content-Type header to urlencoded
oauth = OAuth1Session(
    client_key,
    resource_owner_key=resource_owner_key,
    resource_owner_secret=resource_owner_secret,
    signature_method=oauthlib.oauth1.SIGNATURE_PLAINTEXT,
    signature_type='body',
    verifier='unused')
oauth_tokens = oauth.fetch_access_token(access_token_url)
print(oauth_tokens)
