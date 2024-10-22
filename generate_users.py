import time
import UserFactory
import sys
import csv

fields=[
    'user_id',  # unique
    'first_name',
    'last_name',
    'email',    # unique
    'phone_number',  # unique
    'date_of_birth',
    'address',
    'city',
    'state',
    'country',
    'zip_code',
    'username',  # unique
    'password',
    'account_created',
    'is_active',

]

num_users = 1000000
file_name='generated_users.csv'

if '--num-users' in sys.argv:
    num_users = int(sys.argv[sys.argv.index('--num-users')+1])
if '--file-name' in sys.argv:
    file_name=sys.argv[sys.argv.index('--file-name')+1]



start_time=time.time()

print('Starting user generation...')

with open (file_name,'w',newline='') as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(fields)

factory=UserFactory.UserFactory(num_users,file_name)
factory.create()

end_time=time.time()

print(f"Finished generating users and outputting CSV file: {file_name}")
duration=end_time - start_time
print(f'Duration: { duration :.2f} seconds')
