import json

from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes, parser_classes

from django.contrib.auth import login, authenticate

from .serializers import AccountSerializer
from .models import Account, Publish, PublishAsset, Schedule
from django.http import JsonResponse
import uuid


class AuthRegister(APIView):
    """
    Register a new user.
    """
    serializer_class = AccountSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthLogin(APIView):
    ''' Manual implementation of login method '''
    def post(self, request, format=None):
        data = request.data
        email = data.get('email', None)
        password = data.get('password', None)

        account = authenticate(email=email, password=password)
        # Generate token and add it to the response object
        if account is not None:
            login(request, account)
            return Response({
                'status': 'Successful',
                'message': 'You have successfully been logged into your account.'
            }, status=status.HTTP_200_OK)

        return Response({
            'status': 'Unauthorized',
            'message': 'Username/password combination invalid.'
        }, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def test_link(request):
    print(request.user.id)
    return JsonResponse({"code": "200"})


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def apx_publish(request):
    return_arr = []
    return_pub_arr = []
    publish = Publish.objects.create(
        account_id=request.user.id,
        title=request.data.get('title'),
        uid=request.data.get('uid') if request.data.get('uid') is not None else uuid.uuid4()
    )
    if publish.id:
        for i in request.data.get('assets'):
            publish_assets = PublishAsset.objects.create(
                publish_id=publish.id,
                title=i.get('title'),
                uid=i.get('uid') if i.get('uid') is not None else uuid.uuid4(),
                url=i.get('uri'),
                type_of_assets=i.get('type') if i.get('type') is not None else 'TVSHOW'
            )
        number_of_assets = PublishAsset.objects.filter(publish_id=publish.id).count()
        for pub in PublishAsset.objects.filter(publish_id=publish.id):
            return_pub_arr.append({
                'uri': pub.url
            })

        return_arr.append({
            'title': publish.title,
            'uid': publish.uid,
            'CreatedOn': publish.date_created,
            'CompletedOn': publish.date_completed,
            'uri': return_pub_arr,
            'number_of_assets': number_of_assets
        })
        return JsonResponse({"code": "200", "response": return_arr})

@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def apx_playlist(request, uid):
    return_arr = []
    return_pub_arr = []
    publish = Publish.objects.filter(uid=uid)
    number_of_assets = PublishAsset.objects.filter(publish_id=publish[0].id).count()
    for pub in PublishAsset.objects.filter(publish_id=publish[0].id):
        return_pub_arr.append({
            'uri': pub.url
        })
    return_arr.append({
        'title': publish[0].title,
        'uid': publish[0].uid,
        'CreatedOn': publish[0].date_created,
        'CompletedOn': publish[0].date_completed,
        'uri': return_pub_arr,
        'number_of_assets': number_of_assets
    })
    return JsonResponse({"code": "200", "response": return_arr})


@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
def apx_schedule(request, uid):
    return_arr = []
    return_pub_arr = []
    schedule = Schedule.objects.create(
        title=request.data.get('title'),
        uid=uid,
        is_loop=request.data.get('is_loop')
    )
    if schedule.id:
        publish = Publish.objects.filter(uid=uid)
        number_of_assets = PublishAsset.objects.filter(publish_id=publish[0].id).count()
        for pub in PublishAsset.objects.filter(publish_id=publish[0].id):
            return_pub_arr.append({
                'uri': pub.url
            })
        return_arr.append({
            "title": schedule.title,
            "uid": uid,
            "created_on": schedule.date_created,
            "schedule_on": schedule.date_schedule,
            'uri': return_pub_arr,
            'number_of_assets': number_of_assets
        })
        return JsonResponse({"code": "200", "response": return_arr})