import random
import plotly.figure_factory as pff

dice_sum = []
count = []

for i in range(1, 150) :
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum.append(dice1 + dice2)
    count.append(i)

print(dice_sum)
print(count)

Fig = pff.create_distplot([dice_sum], ["Record"])
Fig.show()