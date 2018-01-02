# from django.http import HttpResponse
# from django.http import JsonResponse
# #from models import User,UserLogging
# from models import UserLogging
# from rest_framework import viewsets 
# from serializers import UserLoggingSerializer
# # from serializers import UserSerializer, UserLoggingSerializer
# from rest_framework.decorators import api_view,detail_route
# from rest_framework.response import Response
# from django.contrib.sessions.models import Session
# from datetime import datetime

 
# # def index(request):
# #     return HttpResponse("Hello, world. You're at the polls index.")

# # class UserViewSet(viewsets.ModelViewSet):
# #     """
# #     API endpoint that allows users to be viewed or edited.
# #     """
# #     queryset = User.objects.all()
# #     serializer_class = UserSerializer
# class UserLoggingViewSet(viewsets.ModelViewSet):
# 	queryset = UserLogging.objects.all()
# 	serializer_class = UserLoggingSerializer
# 	# print("Shabbar shah")
# 	# detail_route()
# 	def Get_Onlinetalker(self,request):
# 		print("shabbarkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkjijijijijijijijiji")
# 		# data = UserLogging.objects.all()
# 		# serializer_class = UserLoggingSerializer

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from TalkingApp.models import UserLogging
from TalkingApp.serializers import UserLoggingSerializer
from datetime import datetime
import pytz


@api_view(['GET'])
def UserLogging_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        UserLoggings = UserLogging.objects.all()
        serializer = UserLoggingSerializer(UserLoggings, many=True)
        return Response(serializer.data)
#All online user API
@api_view(['GET'])
def Get_Online_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        UserLoggings = UserLogging.objects.all()
        currentDate = datetime.now()
        finalList = []

        # currentMillis = currentDate.timestamp()*1000
        currentMillis = unix_time_millis(currentDate) 
        for x in UserLoggings:
        	millisec = unix_time_millis(x.last_Logging_Time)
        	if(currentMillis-millisec<=360000 and x.Talker_Status=='online'):
        		finalList.append(x)
        serializer = UserLoggingSerializer(finalList, many=True)
        return Response(serializer.data)


def unix_time_millis(dt):
	epoch = datetime.utcfromtimestamp(0).replace(tzinfo=pytz.UTC)
	return (dt.replace(tzinfo=pytz.UTC) - epoch).total_seconds() * 1000.0
# Add new user through Talker_Id API and update the old the user.

@api_view(['POST'])
def User_pussh(request):
	if request.method == 'POST':
		loggingObj = {}
		try:
			loggingObj = UserLogging.objects.get(Talker_Id=request.data['Talker_Id'])
			loggingObj.last_Logging_Time = datetime.now()
			loggingObj.Talker_Status='online'
			pass
		except Exception as e:
			loggingObj = UserLogging(Talker_Id=request.data['Talker_Id'],last_Logging_Time=datetime.now(),Talker_Status='online')
		finally:
			loggingObj.save()
			serializer = UserLoggingSerializer(loggingObj,many=False)
		 	return Response(serializer.data)
 
				

