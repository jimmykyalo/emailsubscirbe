from email import message
from django.utils import timezone
import mailchimp_marketing as MailchimpMarketing
from mailchimp_marketing.api_client import ApiClientError
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# Create your views here.
@api_view(['POST'])
def subscribe(request):
    data=request.data
    mailchimp = MailchimpMarketing.Client()
    mailchimp.set_config({
    "api_key": "e255acf5c622271cbe611b46beb55ea0-us12",
    "server": "us12"
    })

    list_id = "7b7d5d669c"
    member_info = {
        "email_address": data['email'],
        "status": "subscribed"
    }

    try:
        response = mailchimp.lists.add_list_member(list_id, member_info)
        
        if response['status'] == 'subscribed':
            return Response('Subscription successful')
        else:
            return Response(response['title'])
    except ApiClientError as error:
        
        return Response(error.text, status=status.HTTP_400_BAD_REQUEST)

    # except:
    #     message = {'detail':'An error occurred please try again later.'}       
    #     return Response(message, status=status.HTTP_400_BAD_REQUEST)