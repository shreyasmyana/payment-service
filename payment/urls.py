from django.urls import path
from payment import views
from payment.views import PaymentView

urlpatterns = [
    path('payments/generate_link/',PaymentView.as_view(), name='payments'),
]