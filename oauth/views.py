from django.shortcuts import redirect, render
from django.http import HttpResponse
import requests


def oauth_login(request):
    client_id = '8'  # OAuth provayderdan olingan clientId
    redirect_uri = 'http://hemis-oauth-test.lc/oauth/callback/'
    authorization_url = 'https://hemis.namdu.uz/oauth/authorize'

    authorization_redirect_url = f'{authorization_url}?client_id={client_id}&redirect_uri={redirect_uri}&response_type=code'
    return redirect(authorization_redirect_url)


def oauth_callback(request):
    code = request.GET.get('code')
    if not code:
        return HttpResponse('Error: No code returned after authentication')

    client_id = '8'  # OAuth provayderdan olingan clientId
    client_secret = 'Vt5dnZtzK_v3vzs0ycsV2uLzrh7zicZUrz4TEiOI'  # OAuth provayderdan olingan clientSecret
    redirect_uri = 'http://hemis-oauth-test.lc/oauth/callback/'
    token_url = 'https://hemis.namdu/oauth/access-token'
    user_info_url = 'https://hemis.namdu.uz/oauth/api/user'

    token_data = {
        'grant_type': 'authorization_code',
        'code': code,
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri
    }
    response = requests.post(token_url, data=token_data)
    access_token = response.json().get('access_token')

    user_info_response = requests.get(user_info_url, headers={'Authorization': f'Bearer {access_token}'})
    user_info = user_info_response.json()

    return render(request, 'oauth/callback.html', {'user_info': user_info})
