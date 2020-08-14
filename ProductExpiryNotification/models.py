from django.db import models
from django.contrib.auth.models import User


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

    best_before = models.IntegerField(default=10, unique=False, blank=True)
    category = models.CharField(max_length=264, choices=ItemCategories.choices, default=ItemCategories.OTHER)
    description = models.TextField(blank=True)
    expiry_date = models.DateField(null=True, unique=False)
    manufactured_date = models.DateField(null=True, unique=False)
    notification_date = models.DateField(null=True, unique=False, blank=True)
    product_name = models.CharField(max_length=264, null=False, unique=True)

    def __str__(self):
        return self.product_name


class ProductImages(models.Model):
    product_id = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='images')
    product_image = models.ImageField(null=True)

    class Meta:
        abstract = True
