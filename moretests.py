<<<<<<< Updated upstream
#classes = []
#while True:
#	course_ID = input("Enter the Course Code or enter \"done\" to finish:")
#	if course_ID.lower() == 'done':
#		break
#	classes.append(course_ID)
#print("You are taking the following classes:")
#for course_ID in classes:
#	print(course_ID)

import nextcord
from nextcord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='Hello')
   async def hello(ctx):
       await
=======
classes = []
while True:
	course_ID = input("Enter the Course Code or enter \"done\" to finish:")
	if course_ID.lower() == 'done':
		break
	classes.append(course_ID)
print("You are taking the following classes:")
for course_ID in classes:
	print(course_ID)   #hhhhhh
>>>>>>> Stashed changes
