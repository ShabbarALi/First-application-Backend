from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def getUserName(request):
	response_data = {}
	response_data['Username'] = 'Shabbar Shah'
	major_data = {}
	major_data['data'] = response_data
	major_data['messageText'] = 'sucessfully sent'
	major_data['messageCode'] = 200
	return JsonResponse(major_data)