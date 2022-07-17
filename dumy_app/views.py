from django.http import HttpRequest, JsonResponse
from django.contrib import messages
from random import choice
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@require_POST
def random_message(request: HttpRequest) -> JsonResponse:
    message_types = [messages.INFO , messages.WARNING , messages.ERROR , messages.SUCCESS]
    messages.add_message(request , choice(message_types) , 'This is a just dumy message')
    return JsonResponse({'status' : True})