from django_cron import CronJobBase, Schedule
from .models import Product, UserProfile
from datetime import date
from django.core.mail import send_mail
from tabulate import tabulate

""" Run cron jobs to find objects about to expire.  """


class ExpiryNotificationCronJob(CronJobBase):
    RUN_EVERY_MIN = 5
    # RUN_AT_TIME = ['11:30', '12:00']
    schedule = Schedule(run_every_mins=RUN_EVERY_MIN)
                        # , run_at_times=RUN_AT_TIME)
    code = 'ExpiryNotificationCronJob'  # a unique name for CRON job

    def do(self):
        for user_profile in UserProfile.objects.all():
            product_set = list(Product.objects.filter(bought_by=user_profile))
            product_ids = [product_item.id for product_item in product_set]
            products = Product.objects.filter(id__in=product_ids)
            products_about_to_expire = []
            for product in products:
                if date.today() == product.notification_date:
                    products_about_to_expire.append(product)
                    """ TODO : Update the notification date according to the days remaining in expiry of the product. 
                        TODO : Make user enter the notification date or ask them how many days before the expiry 
                        date they want notification for the product?
                    """

            if products_about_to_expire:
                email_body = self.email_body_template(products_about_to_expire)
                print(email_body)
                res = send_mail(
                    'Products About To Expire',
                    email_body,
                    'expirynotifier@gmail.com',
                    [user_profile.user.email],
                    fail_silently=False,
                )
""" Template for expiry notification email.  """
    def email_body_template(self, products):
        heading = 'Hello, \n\nThese products are about to expire.\n\n'
        table_headers = (['Product Name', 'Expiry Date', 'Days Remaining'])
        table = []
        for product in products:
            # print("Product Name: {} Expiry Date: {}".format(product,product.expiry_date))
            days_before_expiry = product.expiry_date - date.today()
            table.append([product, product.expiry_date, days_before_expiry])
        final_message = heading + tabulate(table, headers=table_headers, tablefmt='fancy_grid')
        return final_message
