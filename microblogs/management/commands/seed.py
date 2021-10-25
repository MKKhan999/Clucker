from django.core.management.base import BaseCommand,CommandError
from faker import Faker
import faker.providers
from microblogs.models import User

class Command(BaseCommand):
    def __init__(self):
        super().__init__()
        self.fake=Faker('en_GB')


    def handle(self, *args, **options):
        for i in range(100):
            self.user = User.objects.create_user(
                '@'+self.fake.user_name(),
                first_name=self.fake.first_name(),
                last_name=self.fake.last_name(),
                email=self.fake.email(),
                password=self.fake.password(),
                bio=self.fake.text())