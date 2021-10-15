"""Update users table with country and city"""
from posts.models import User

peru_users = User.objects.exclude(email__endswith='@platzi.com')
platzi_users = User.objects.filter(email__endswith='@platzi.com')

for user in platzi_users:
    user.country = 'Colombia'
    user.city = 'Bogotá'
    user.save()
    print(user.first_name, '-', user.country, '-', user.city)

for user in peru_users:
    user.country = 'Peru'
    user.city = 'Lima'
    user.save()
    print(user.first_name, '-', user.country, '-', user.city)