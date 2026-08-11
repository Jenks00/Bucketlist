from django.urls import path
from .views import To_doList, To_doCreate, To_doUpdate, To_doDelete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', To_doList.as_view(), name="task"),
    path('to_do-create/', To_doCreate.as_view(), name="to_do-create"),
    path('login/', CustomLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(next_page='login'), name="logout"),
    path('register/', RegisterPage.as_view(), name="register"),
    path('to_do-update/<int:pk>/', To_doUpdate.as_view(), name="to_do-update"),
    path('to_do-delete/<int:pk>/', To_doDelete.as_view(), name="to_do-delete")

]