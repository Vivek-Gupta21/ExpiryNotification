from faker import Faker
import os
import sys
import unicodedata
import django
import random

""" @:link https://www.diveinto.org/python3/your-first-python-program.html#importsearchpath
    Need to insert Project path in Python Import Search Path, read more about it on the link. """

sys.path.insert(0, r'C:\Users\Vivek\PycharmProjects\ExpiryNotification')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ExpiryNotification.settings')
django.setup()

# from ProductExpiryNotification.models import Product, UserProfile, Counter, counters_initialized
#
# """ To use Pymongo commands, connect using these lines:
#     >: my_client = pymongo.MongoClient("mongodb://localhost:27017/")
#     >: database = my_client["product_expiry_notification"]
#     >: user_collection = database["UserProfile"]"""
#
#
# def get_faker():
#     return Faker()
#
#
# def get_random_category():
#     category = random.choices(Product.ItemCategories.choices)[0][0]
#     return category
#
#
# def get_random_notification_mode():
#     return random.choices(UserProfile.NotificationTypes.choices)[0][0]
#
#
# def get_random_product():
#     product_list = ['Pears', 'Butter', 'Soap', 'Bottle', 'Mouse', 'Oil', 'Notebooks', 'Curd', 'Chocolate', 'Coffee',
#                     'Peanut Butter', 'Jam']
#     return random.choices(product_list)[0]
#
#
# def initialize_counter():
#     # for key, val in counters_initialized.items():
#     #     if val:
#     values = {
#         "_id": "product_id",
#         "sequence_value": 0
#     }
#     Counter.objects.mongo_insert_one(values)


# def get_next_sequence_value(sequenceName):
#     sequenceValue = 1
#     sequenceDocument = Counter.objects.filter(_id = sequenceName)
#     for entry in sequenceDocument:
#         sequenceValue += entry.sequence_value
#     Counter.objects.update(sequence_value = sequenceValue)
#     return sequenceValue


# def populate_user(total_entries=1):
#     fake = get_faker()
#     for entry in range(total_entries):
#         fake_profile = fake.profile(fields = ['username', 'name', 'mail'])
#         fake_contact_number = fake.bothify(text = '##########')
#         fake_notify_by = get_random_notification_mode()
#         values = {
#             'user_name': fake_profile['username'],
#             'email_id': fake_profile['mail'],
#             'full_name': fake_profile['name'],
#             'contact_no': fake_contact_number,
#             'notify_by': fake_notify_by
#         }
#         UserProfile.objects.mongo_insert_one(values)
#
#
# def populate_products(total_entries=1):
#     fake = get_faker()
#     # date_format = "%Y-%m-%d"
#     for entries in range(total_entries):
#         fake_product_id = str(get_next_sequence_value("product_id"))
#         # fake_manufacturing_date = fake.date()
#         fake_best_before = fake.date()
#         # fake_expiry_date = fake.date()
#         # fake_notification_date = datetime.strptime(fake_expiry_date, date_format) - timedelta(days = 10)
#         values = {
#             '_id': fake_product_id,
#             'product_name': get_random_product(),
#             # 'manufactured_date': fake_manufacturing_date,
#             'best_before': fake_best_before,
#             # 'expiry_date': fake_expiry_date,
#             # 'notification_date': fake_notification_date,
#             'category': get_random_category()
#         }
#
#         Product.objects.mongo_insert_one(values)
#
#
# def generate_username(full_name):
#     name = unicodedata.normalize('NFKD', full_name.lower()).encode('ASCII', 'ignore')
#     name = name.decode().split(' ')
#     last_name = name[-1]
#     first_name = name[0]
#     username = '%s%s' % (first_name, last_name)
#     if len(list(UserProfile.objects.mongo_find({'user_name': username}))) > 0:
#         username = '%s%s' % (first_name[0], last_name)
#         if len(list(UserProfile.objects.mongo_find({'user_name': username}))) > 0:
#             username = '%s%s' % (first_name, last_name[0])
#             if len(list(UserProfile.objects.mongo_find({'user_name': username}))) > 0:
#                 query = {"user_name": {"$regex": "^%s[1-9]{1,}$" % first_name}}
#                 cursorRecords = UserProfile.objects.mongo_find(query)
#                 users = [record['user_name'] for record in cursorRecords]
#                 if len(users) > 0:
#                     last_number_used = sorted(map(lambda x: int(x.replace(first_name, '')), users))
#                     number = last_number_used[-1] + 1
#                     username = '%s%s' % (first_name, number)
#                 else:
#                     username = '%s%s' % (first_name, 1)
#     return username
#
#
if __name__ == '__main__':
    print('Initializing Values:')
    # initialize_counter()
    print('Populating Data')
    # populate_user()
    # populate_products()
    # Product.objects.mongo_delete_many({})
    # UserProfile.objects.mongo_delete_many({})
    # print(generate_username("Vivek Gupta"))
    print('Populating Data complete')
