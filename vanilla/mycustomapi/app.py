from django.conf.urls import url

from mycustomapi.views import root, product, category

from oscarapi.app import RESTApiApplication


class MyRESTApiApplication(RESTApiApplication):

    def get_urls(self):
        urls = [
            url(r'^$', root.api_root, name='api-root'),
            url(r'^products/$',
                product.ProductList.as_view(), name='product-list'),
            url(r'^categories/$',
                category.CategoryList.as_view(), name='category-list'),
            url(r'^categories/(?P<pk>[0-9]+)/$',
                category.CategoryDetail.as_view(), name='category-detail'),
            url(r'^categories/(?P<pk>[0-9]+)/products/$',
                category.CategoryProductsList.as_view(), name='category-product-list'),
        ]

        return urls + super(MyRESTApiApplication, self).get_urls()

application = MyRESTApiApplication()
