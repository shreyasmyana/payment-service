import json
from abc import ABC, abstractmethod

import razorpay

from PaymentService import settings


class PaymentGateway(ABC):
    @abstractmethod
    def generate_payment_link(self, order_id, amount):
        pass


class RazorPaymentGateway(PaymentGateway):
    def __init__(self):
        self.client = razorpay.Client(
            auth=(settings.RAZORPAY_ID, settings.RAZORPAY_SECRET),
        )

    def generate_payment_link(self, order_id, amount):
        payment_data = {
            "amount": amount,
            "currency": "INR",
            "description": "For XYZ purpose",
            "customer": {
                "name": "Shreyas ",
                "email": "Shreyas@gmail.com",
                "contact": "+918944524152"
            },
            "notify": {
                "sms": True,
                "email": True
            },
            "reminder_enable": True,
            "callback_url": "https://google.com/",
            "callback_method": "get"
        }

        payment_link = self.client.payment_link.create(payment_data)
        return payment_link
