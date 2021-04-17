from django.urls import path

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name="store"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),

	path('update_item/', views.updateItem, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('fan/', views.fan, name="fan"),
	path('details/', views.details, name="details"),
	path('contact/', views.contact, name="contact"),
	path('paypal1/', views.paypal1, name="paypal1"),

	# pdf url

	path('index', views.index,name="index"),
    path('pdf_view/', views.ViewPDF.as_view(), name="pdf_view"),
    path('pdf_download/', views.DownloadPDF.as_view(), name="pdf_download"),

]