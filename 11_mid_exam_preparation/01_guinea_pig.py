food = float(input())*1000
hay = float(input())*1000
cover = float(input())*1000
pig_weight = float(input())*1000
flag = False
for day in range(1, 31):
  food -= 300
  if day % 2 == 0:
    hay -= 0.05*food
  if day % 3 == 0:
    cover -= (1/3)*pig_weight
  if food <= 0 or hay <= 0 or cover <= 0:
    flag = True
    break
if not flag:
  print(f"Everything is fine! Puppy is happy! Food: {(food)/1000:.2f}, Hay: {(hay)/1000:.2f}, Cover: {(cover)/1000:.2f}.")
else:
  print("Merry must go to the pet store!")