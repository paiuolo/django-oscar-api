from oscar.core.loading import get_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from oscarapi.utils import OscarHyperlinkedModelSerializer


Category = get_model('catalogue', 'Category')


class CategorySerializer(OscarHyperlinkedModelSerializer):
    products = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ('url', 'id', 'name', 'slug', 'products')
        
    def get_products(self, obj):
        request = self.context['request']
        return reverse('category-product-list', request=request, kwargs={'pk': obj.pk})