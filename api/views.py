from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from providers.models import Provider
from providers.serializers import ProviderSerializer


@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProviderSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save()
        print(instance)
        # data = serializer.data
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)
    # instance = Provider.objects.all().order_by("?").first()
    # data = {}
    # if instance:
    #     data = ProviderSerializer(instance).data
    # data = model_to_dict(instance, fields=['id', 'name', 'language'])
    # print(request.GET)  # url query params
    # body = request.body  # byte string
    # data = {}
    # try:
    #     data = json.loads(body)  # convert byte string json to python dict
    # except:
    #     pass
    # print(data)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # return Response(data)
