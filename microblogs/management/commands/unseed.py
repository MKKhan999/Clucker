from django.core.management.base import BaseCommand,CommandError
from faker import Faker
import faker.providers
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.fake=Faker('en_GB')

    def superuser(self):
        count = 0
        for i in range(User.objects.all().count()):
            user1 = User.objects.all()[i]
            if (user1.is_superuser):
                count+=1
        return count
    def handle(self, *args, **options):
        length = User.objects.all().count()
        while length != self.superuser():
            user1 = User.objects.all()[length-1]
            if (user1.is_superuser):
                length-=1
            else:
                User.objects.all()[length-1].delete()
                length-=1