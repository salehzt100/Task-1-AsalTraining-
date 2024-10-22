import time
import sys
import User

num_users:int = 1000000
file_name:str = 'generated_users.csv'

if '--num-users' in sys.argv:
   num_users = int(sys.argv[sys.argv.index('--num-users') + 1])
if '--file-name' in sys.argv:
    file_name = sys.argv[sys.argv.index('--file-name') + 1]

# create instance from user class
model=User.User(num_users,file_name)


# start time
start_time = time.time()

print('Starting user generation...')

# add header fields
model.addHeaderFieldsToCsvFile()

# factory create
model.addGeneratedUserWithFakerToCsvFile()

# end time
end_time = time.time()

print(f"Finished generating users and outputting CSV file: {file_name}")

# calculate duration
duration = end_time - start_time
print(f'Duration: {duration :.2f} seconds')




