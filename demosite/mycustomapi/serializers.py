from oscar.core.loading import get_class

from oscarapi.serializers.checkout import PriceSerializer
from oscarapi.serializers.product import (
    ProductImageSerializer, ProductLinkSerializer)

from rest_framework import serializers


Selector = get_class('partner.strategy', 'Selector')


class MyProductLinkSerializer(ProductLinkSerializer):
    images = ProductImageSerializer(many=True, required=False)
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        request = self.context.get('request')
        user = request.user if request is not None else None
        strategy = Selector().strategy(request=request, user=user)
        price = strategy.fetch_for_product(obj).price
        ser = PriceSerializer(
            price, context={'request': request})
        return ser.data

    class Meta(ProductLinkSerializer.Meta):
        fields = ('url', 'id', 'title', 'images', 'price')
