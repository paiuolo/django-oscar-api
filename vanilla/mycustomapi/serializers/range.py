from rest_framework import serializers
from rest_framework.reverse import reverse
from oscar.core.loading import get_model
from oscarapi.utils import OscarHyperlinkedModelSerializer


Range = get_model('offer', 'Range')


class RangeSerializer(OscarHyperlinkedModelSerializer):
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Range
        fields = ('url', 'id', 'name', 'slug', 'products')
        
    def get_products(self, obj):
        request = self.context['request']
        return reverse('range-product-list', request=request, kwargs={'pk': obj.pk})