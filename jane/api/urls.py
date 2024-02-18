from django.urls import path

from .views import CreditorView, DebtorView

urlpatterns = [
    path("creditor", CreditorView.as_view()),
    path("debtor", DebtorView.as_view()),
]
