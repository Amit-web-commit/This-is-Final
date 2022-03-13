from django.urls import path, include
app_name = 'FoodApp'
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.loginPage, name='loginPage'),
    path('signup', views.signup, name='signup'),
    path('product', views.product, name='product'),
    path('product/<int:id>', views.productdetail, name='productdetail'),
    path('customizemenu', views.customizeMenu, name= 'customizemenu'),
    path('reservetable', views.reserveTable, name='reserveTable'),
    path('contact', views.contact,name='contact' ),
    path('carttotal', views.carttotal, name='carttotal'),
    path('edit', views.editIngredients, name='editIngredients'),
    # path('submit_review', views.submitReview, name='submitReview')
    path('submitReview/<int:id>', views.submit_review, name='submit_review'),
    path('add/<int:id>', views.cart_add, name='cart_add'),
    path('remove/<int:id>', views.cart_remove, name='cart_remove')
    
]