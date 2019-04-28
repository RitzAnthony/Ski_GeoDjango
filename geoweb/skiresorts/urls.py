from django.urls import path

from . import views

urlpatterns = [
    path('', views.resorts_view, name='resorts'),
    path('popup/', views.popup_view, name='popup'),
    path('resort_popup/<int:skiresort_id>', views.resort_popup_view, name='resort_popup'),
    path('<int:skiresort_id>', views.details_view, name='details'),
    path('updateslope/<int:slope_id>', views.update_slope_view, name='updateslope'),

]