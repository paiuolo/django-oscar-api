from rest_framework import serializers
from oscarapi.serializers.product import PartnerSerializer
from oscarapi.utils import OscarHyperlinkedModelSerializer


class PartnerSerializer(ProductLinkSerializer):
    images = ProductImageSerializer(many=True, required=False)
    title = serializers.CharField(source='get_title')
    categories = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='name',
        source='get_categories')

    class Meta(ProductLinkSerializer.Meta):
        fields = overridable(
            'OSCARAPI_PRODUCT_FIELDS', default=(
                'url', 'id', 'title', 'images', 'categories'
            ))
