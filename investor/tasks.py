from celery import shared_task
from django.utils import timezone
from .models import Purchase, UserAccount
from decimal import Decimal
import time

@shared_task
def generate_profit():
    now = timezone.now()
    purchases = Purchase.objects.filter(purchase_date__lte=now - timezone.timedelta(seconds=30))
    for purchase in purchases:
        profit = purchase.item.price * Decimal('0.01')  # For example, 0.01% profit per 2 seconds for testing
        purchase.profit += profit
        purchase.save()

        # Update the user's account balance
        user_account = UserAccount.objects.get(user=purchase.user)
        user_account.balance += profit
        user_account.save()

    # Schedule the task to run again after 2 seconds
    time.sleep(30)
    generate_profit.delay()

