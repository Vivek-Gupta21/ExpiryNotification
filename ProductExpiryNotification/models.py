from datetime import date, timedelta, datetime
from django.db import models
from django.contrib.auth.models import User

DEFAULT_DATE = datetime(1960, 1, 1).date()


class UserProfile(models.Model):
    class NotificationTypes(models.TextChoices):
        MAIL = 'MAIL'
        TEXT = 'TEXT'

    bought = models.ManyToManyField('Product', related_name='bought_by', blank=True)
    contact_no = models.CharField(max_length=10, null=True, unique=False, blank=True)
    notify_by = models.CharField(max_length=10, choices=NotificationTypes.choices, default=NotificationTypes.MAIL)
    profile_pic = models.ImageField(upload_to='ProductExpiryNotification/profile_pics', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Product(models.Model):
    class ItemCategories(models.TextChoices):
        BEVERAGES = 'Beverages'
        DOCUMENTS = 'Documents'
        FRUITS = 'Fruits'
        GROCERIES = 'Groceries'
        MEDICINES = 'Medicines'
        VEGETABLES = 'Vegetables'
        OTHER = 'Other'

    best_before = models.IntegerField(default=50, unique=False, blank=True, null=True)
    category = models.CharField(max_length=20, choices=ItemCategories.choices, default=ItemCategories.OTHER)
    description = models.TextField(blank=True, max_length=240)
    expiry_date = models.DateField(null=True, unique=False)
    manufactured_date = models.DateField(null=True, unique=False)
    notification_date = models.DateField(null=True, unique=False, blank=True)
    product_name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return self.product_name

    # TODO : Notification Date not getting updated. Find the source of bug and resolve it!
    # Update the notification date according to the days remaining in expiry of the product.
    def update_notification_date(self):
        days_remaining = (self.expiry_date - self.notification_date).days
        if days_remaining > 5:
            self.notification_date = self.expiry_date + timedelta(days=5)
        elif 5 >= days_remaining > 3:
            self.notification_date = self.expiry_date + timedelta(days=3)
        elif 3 >= days_remaining > 1:
            self.notification_date = self.expiry_date + timedelta(days=1)
        else:
            self.notification_date = DEFAULT_DATE
        self.save()

    @staticmethod
    def products_about_to_expire():
        expiring_product_user_dict = {}
        for user_profile in UserProfile.objects.all():
            products_bought_by_user = list(Product.objects.filter(bought_by__user=user_profile.user))
            product_ids = [product.id for product in products_bought_by_user]
            products = Product.objects.filter(id__in=product_ids)
            products_expiring = []
            for product in products:
                if date.today() == product.notification_date:
                    products_expiring.append(product)
            expiring_product_user_dict[user_profile] = products_expiring
        return expiring_product_user_dict


class ProductImages(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    product_image = models.ImageField(null=True)

    class Meta:
        abstract = True
