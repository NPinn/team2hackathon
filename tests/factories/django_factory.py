import factory
from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    first_name = "first_name"
    last_name = factory.Faker("last_name")
    is_staff = False
    is_active = True
    is_superuser = False
