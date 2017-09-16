from mycustomapi.serializers.product import MyProductLinkSerializer
from oscarapi.views import basic


class ProductList(basic.ProductList):
    serializer_class = MyProductLinkSerializer
