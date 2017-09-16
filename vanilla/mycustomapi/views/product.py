from oscarapi.views import basic

from ..serializers.product import MyProductLinkSerializer


class ProductList(basic.ProductList):
    serializer_class = MyProductLinkSerializer
