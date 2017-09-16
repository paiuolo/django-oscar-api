from oscar.core.loading import get_model
from rest_framework import generics

from ..serializers.category import CategorySerializer
from ..serializers.product import MyProductLinkSerializer


Category = get_model('catalogue', 'Category')
Product = get_model('catalogue', 'Product')


class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryDetail(generics.RetrieveAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryProductsList(generics.ListAPIView):
    serializer_class = MyProductLinkSerializer

    def get_queryset(self):
        category_pk = self.kwargs['pk']

        return Product.objects.filter(categories__in=[category_pk])