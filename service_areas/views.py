from rest_framework import generics

from .models import ServiceArea
from .serializers import ServiceAreaSerializer


class ServiceAreaListCreateAPIView(generics.ListCreateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user
        print(f"request data {self.request.data}")
        print(serializer.validated_data)
        instance = serializer.save()


service_area_list_create_view = ServiceAreaListCreateAPIView.as_view()


class ServiceAreaDetailAPIView(generics.RetrieveAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    # lookup_field = 'pk'
    # def get_queryset(self):
    #     pass


service_area_detail_view = ServiceAreaDetailAPIView.as_view()


class ServiceAreaUpdateAPIView(generics.UpdateAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


service_area_update_view = ServiceAreaUpdateAPIView.as_view()


class ServiceAreaDestroyAPIView(generics.DestroyAPIView):
    queryset = ServiceArea.objects.all()
    serializer_class = ServiceAreaSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


service_area_destroy_view = ServiceAreaDestroyAPIView.as_view()
