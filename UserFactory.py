from faker import Faker
from typing import Generator


class UserFactory():

    def __init__(self, num_users: int) -> None:
        self.num_users = num_users

    """
      generate row of fake data by faker module, and yield each row to addGeneratedUserWithFakerToCsvFile() method
       to store it in csv file  
    """
    def createUserWithFakeData(self)->Generator:
        fake = Faker()
        for i in range(self.num_users):
            row = [
                i+1,    #unique
                fake.first_name(),
                fake.last_name(),
                fake.unique.email(),   #unique
                fake.unique.phone_number(),  #unique
                fake.date_of_birth(),
                fake.address(),
                fake.city(),
                fake.state(),
                fake.country(),
                fake.zipcode(),
                fake.unique.user_name(),    #unique
                fake.password(),
                fake.past_date(),
                fake.boolean()
            ]
            yield row


