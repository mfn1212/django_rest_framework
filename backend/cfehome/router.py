from products.viewset import ProductViewSet
from rest_framework.routers import DefaultRouter
router  = DefaultRouter() 
router.register("product_abc",ProductViewSet,basename='product')
urlpatterns = router.urls
print(urlpatterns)
