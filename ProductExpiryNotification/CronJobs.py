# from django_cron import CronJobBase, Schedule
# from .models import Product
# from datetime import date
# from django.core.mail import send_mail
# from tabulate import tabulate
#
#
# # TODO : Make user enter the notification date or ask them how many days before the expiry date they want
# #  notification for the product?
#
# # Composes the template for expiry notification E-mail.
# def email_body_template(products):
#     heading = 'Hello, \n\nThese products are about to expire.\n\n'
#     table_headers = (['Product Name', 'Expiry Date', 'Days Remaining'])
#     table = []
#     for product in products:
#         days_before_expiry = product.expiry_date - date.today()
#         table.append([product, product.expiry_date, days_before_expiry])
#     final_message = heading + tabulate(table, headers=table_headers, tablefmt='fancy_grid')
#     return final_message
#
#
# def send_mail_to_user(user, products):
#     email_body = email_body_template(products)
#     res = send_mail('Products About To Expire', email_body, 'expirynotification@gmail.com',
#                     [user.user.email], fail_silently=False)
#
#
# # Run cron jobs to find objects about to expire.
# class ExpiryNotificationCronJob(CronJobBase):
#     RUN_EVERY_MIN = 1
#     schedule = Schedule(run_every_mins=RUN_EVERY_MIN)
#     code = 'ExpiryCronJob'  # a unique name for CRON job
#
#     def do(self):
#         expiring_product_user_dict = Product.products_about_to_expire()
#         for user, products in expiring_product_user_dict.items():
#             if products:
#                 send_mail_to_user(user, products)
#                 for product in products:
#                     product.update_notification_date()
