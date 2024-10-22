from faker import Faker
import csv

class UserFactory:

    def __init__(self,num,file_name):
        self.num = num
        self.file_name = file_name

    def create(self):
        fake = Faker()
        for i in range(self.num):
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
            with open(f'{self.file_name}', 'a') as csvfile:
                writer =csv.writer(csvfile,delimiter='|',quoting=csv.QUOTE_ALL)
                writer.writerow(row)




