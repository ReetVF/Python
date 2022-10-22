###Import###
import random

##Random Zahl##

#-Normanl#

random_ziffer = random.randint(0,1500)

print(f"your random ziffer is {random_ziffer}")

#Function#

async def random():
  ziffer = random.randint(0,1500)
  return ziffer

print(f"your ziffer is {random}")

#random Choiche#

tiere = ["dog", "cat", "horse"]
radom_choice = random.choice(tiere)
print(f"your tier are {radom_choice}")
