from products.viewset import ProductGenericViewSet
from rest_framework.routers import DefaultRouter
router  = DefaultRouter() 
router.register("product_abc",ProductGenericViewSet,basename='product')
urlpatterns = router.urls
print(urlpatterns)
