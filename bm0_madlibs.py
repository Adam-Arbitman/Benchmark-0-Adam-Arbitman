import random

dice = random.randint(1,3)
print: story
verb = str(input("please input a verb(action) word: "))
noun = str(input("please input a noun(person,place,thing) word: "))
adjective = str(input("please input a adjective(describes) word: "))
name = str(input("please write your name: "))




if dice == 1: 
	
	print (f"I {verb} to the {noun}, and got some sandwiches. The sandwiches were pretty {adjective}")
	print(f"When {name} went to the park {name} saw the most {noun} {adjective} thing on a bench")

if dice == 2:
	
	print(f"{name} went to go {verb} and along the way {name} met with frankie")
	print(f"They met at the {noun} and went to go into their {verb}")
	print(f"then they went shopping and felt the {adjective} coat.")



if dice == 3:
	
	print(f" {name} went to the park and there was a very {adjective} and insane homeless guy in the {noun}")
	print(f"this shocked {name} because why is a homeless man going through the {noun} doing {verb}")