from rest_framework import generics

from .models import Provider
from .serializers import ProviderSerializer


class ProviderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        instance = serializer.save()


provider_list_create_view = ProviderListCreateAPIView.as_view()


class ProviderDetailAPIView(generics.RetrieveAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    # lookup_field = 'pk'
    # def get_queryset(self):
    #     pass


provider_detail_view = ProviderDetailAPIView.as_view()


class ProviderUpdateAPIView(generics.UpdateAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()


provider_update_view = ProviderUpdateAPIView.as_view()


class ProviderDestroyAPIView(generics.DestroyAPIView):
    queryset = Provider.objects.all()
    serializer_class = ProviderSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


provider_destroy_view = ProviderDestroyAPIView.as_view()
