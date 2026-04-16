import random
import statistics

def Rolling_dice(dice,faces,rolls, weights,bins):
    """
    step1 : is to create a list of the dice faces in relation to the weights
    step2: then am gonna randomize the outcome for each dice for 1000 rolls
    step3: sum up the outcomes of the dices to create a new list of the sums  which will range from 2 up to 12.
    we can't have 1 because we don't have a dice face of zero so the sums min is 2(dice1: 1 . dice2:1) to max ((dice1: 6 . dice2:6))
    step4: use a dictionary for the frequency distribution with outcome as key and the number the outcome appears as the value.
    step5: plot the histogram using bins, as in floor dividing the value of the dict by 10 so that we don't have remainders
    step6: use the statistics module to determine the mean, median, mode, varience, std.
    """   
    dice1_sort = []
    dice1_faces = ['1','2','3','4','5','6']
    for i, j in zip(dice1_faces,weights):
        dice1_sort.extend([i] *j)
    # print(dice1_sort)
    dice1 = [int(i) for i in dice1_sort]
    # print(dice1)
    dice1_rolls = []
    dice1_rolls = []
    for num in range(rolls):
        i = random.choice(dice1)
        dice1_rolls.append(i)
        
    dice2_sort = []
    dice2_faces = ['1','2','3','4','5','6']
    for i, j in zip(dice2_faces,weights):
        dice2_sort.extend([i] *j)
    # print(dice2_sort)
    dice2 = [int(i) for i in dice2_sort]
    # print(dice2)
    dice2_rolls = []
    dice2_rolls = []
    for num in range(rolls):
        j = random.choice(dice2)
        dice2_rolls.append(j)
    dice_sums = [d1 + d2 for d1, d2 in zip(dice1_rolls, dice2_rolls)]
    frequency_distribution = {x: dice_sums.count(x) for x in set(dice_sums)}
    print("Frequency distribution: ")
    print("Outcome    Frequency")
    for key, value in frequency_distribution.items():
        print(f"{key}          {value}")
    histo = "*"
    freq = []
    for value in frequency_distribution.values():
        new_value = value // bins
        freq.append(new_value)
    print() 
    print("Histrogram")
   
    for i, value in enumerate(frequency_distribution.keys()):
    
        print(f"{value}: {histo * freq[i]}")

    Mean = statistics.mean(freq)
    Median = statistics.median(freq)
    Mode = statistics.mode(freq)
    Variance = statistics.variance(freq)
    Standard = statistics.stdev(freq)
    print() 
    print("Summary Stastics:")
    print(f"Mean: {round(Mean,2)}")
    print(f"Median: {Median}")
    print(f"Mode: {Mode}")
    print(f"Variance: {round(Variance,2)}")
    print(f"Standard Deviation: {round(Standard,2)}")
    return ""

# dice stimulator new




       
    



print((Rolling_dice(2,6,1000,[1,1,1,1,2,2],10)))
    