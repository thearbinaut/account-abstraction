
# Email Automation Script

import requests

# Mailchimp API credentials
API_KEY = 'your_mailchimp_api_key'
SERVER_PREFIX = 'your_server_prefix'
LIST_ID = 'your_list_id'

# Email content
SUBJECT = 'Welcome to Our Newsletter'
CONTENT = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome</title>
</head>
<body>
    <h1>Welcome to Our Newsletter</h1>
    <p>Thank you for subscribing to our newsletter. Stay tuned for updates and promotions.</p>
</body>
</html>
"""

def add_subscriber(email):
    url = f'https://{SERVER_PREFIX}.api.mailchimp.com/3.0/lists/{LIST_ID}/members'
    data = {
        'email_address': email,
        'status': 'subscribed'
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.post(url, json=data, headers=headers)
    return response.status_code

def send_email(email):
    url = f'https://{SERVER_PREFIX}.api.mailchimp.com/3.0/campaigns'
    data = {
        'type': 'regular',
        'recipients': {
            'list_id': LIST_ID
        },
        'settings': {
            'subject_line': SUBJECT,
            'title': 'Welcome Campaign',
            'from_name': 'Your Company',
            'reply_to': 'your_email@example.com'
        }
    }
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.post(url, json=data, headers=headers)
    campaign_id = response.json().get('id')
    
    if campaign_id:
        url = f'https://{SERVER_PREFIX}.api.mailchimp.com/3.0/campaigns/{campaign_id}/content'
        data = {
            'html': CONTENT
        }
        response = requests.put(url, json=data, headers=headers)
        
        if response.status_code == 200:
            url = f'https://{SERVER_PREFIX}.api.mailchimp.com/3.0/campaigns/{campaign_id}/actions/send'
            response = requests.post(url, headers=headers)
            return response.status_code
    return response.status_code

if __name__ == '__main__':
    email = 'subscriber@example.com'
    add_subscriber(email)
    send_email(email)
