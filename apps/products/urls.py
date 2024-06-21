from rest_framework import routers

from apps.products import views

app_name = 'api_products'

router = routers.SimpleRouter()
router.register('categories', views.CategoryAPIViewSet, basename='category')
router.register('products', views.ProductAPIViewSet, basename='product')
router.register('brands', views.BrandAPIViewSet, basename='brand')

urlpatterns = []

urlpatterns += router.urls
