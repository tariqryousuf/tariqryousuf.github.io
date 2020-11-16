import csv


def non_linear_quantization(a):
    if (abs(a) < 0.05):
        return_value = 0
    elif (abs(a) < 1.0):
        if (a > 0.0):
            return_value = (int((a + 0.1) * 10))
        else:
            return_value = (int((a - 0.1) * 10))
    elif ((a > 0.0)):
        if (abs(a) < 1.2):
            return_value = 11
        elif (abs(a) < 1.4):
            return_value = 12
        elif (abs(a) < 1.6):
            return_value = 13
        elif (abs(a) < 1.8):
            return_value = 14
        elif (abs(a) < 2.0):
            return_value = 15
        else:
            return_value = 16
    else:
        if (abs(a) < 1.2):
            return_value = -11
        elif (abs(a) < 1.4):
            return_value = -12
        elif (abs(a) < 1.6):
            return_value = -13
        elif (abs(a) < 1.8):
            return_value = -14
        elif (abs(a) < 2.0):
            return_value = -15
        else:
            return_value = -16

    return return_value

results = []
with open("downward_arrow_1.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)


for i in range(len(results)):
    #print("{" + str(int(results[i][0])) + ", " + str(int(results[i][1])) + ", " + str(int(results[i][2])) + "},")
    print("{" + str(non_linear_quantization(results[i][0])) + ", " + str(non_linear_quantization(results[i][1])) + ", " + str(non_linear_quantization(results[i][2])) + "},")
    
