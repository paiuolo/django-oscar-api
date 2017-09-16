from oscar.core.loading import get_model
from rest_framework import generics

from ..serializers.range import RangeSerializer
from ..serializers.product import MyProductLinkSerializer


Range = get_model('offer', 'Range')
Product = get_model('catalogue', 'Product')


class RangeList(generics.ListAPIView):
    serializer_class = RangeSerializer
    queryset = Range.objects.all()
    
class RangeDetail(generics.RetrieveAPIView):
    serializer_class = RangeSerializer
    queryset = Range.objects.all()
    
class RangeProductsList(generics.ListAPIView):
    serializer_class = MyProductLinkSerializer

    def get_queryset(self):
        range_pk = self.kwargs['pk']
        range = Range.objects.get(pk=range_pk)
        return range.all_products()