import json 
import numpy as np
import matplotlib.pyplot as plt
import math

jj = open("output.json").read()

algorithms = ["BSPPI","BSUNC", "BSWN"]
typeOfSorter = ["INTEGER", "STRING", "DUMMY"]
sizeOfList = ["SMALL", "MEDIUM", "LARGE"]
statusList = ["RG", "AS", "SB"]

SIZE = {"SMALL": 10, "MEDIUM": 100, "LARGE": 1000}
COLOR = {"SMALL": 'r', "MEDIUM": 'g', "LARGE": 'b'}

data = json.loads(jj)

for typeS in typeOfSorter:
  for stat in statusList:
    for sizeL in sizeOfList:
      numpy_array_1 = np.array(data["BSPPI"][typeS][sizeL][stat]) * 1e-6
      numpy_array_2 = np.array(data["BSWN"][typeS][sizeL][stat]) * 1e-6
      numpy_array_3 = np.array(data["BSUNC"][typeS][sizeL][stat]) * 1e-6
      numpy_array = np.transpose(np.stack((numpy_array_1, numpy_array_2, numpy_array_3)))

      plt.title(f"{typeS}, {sizeL}, {stat}")
      plt.xlabel("Iteration #")
      plt.ylabel("Total time (ms)")
      _ = plt.plot(numpy_array_1, 'r.', label="BubbleSortPassPerItem")
      _ = plt.plot(numpy_array_2, 'g.', label="BubbleSortWhileNeeded")
      _ = plt.plot(numpy_array_3, 'b.', label="BubbleSortUntilNoChange")
      plt.legend()
      plt.savefig(f"figures/{typeS}_{sizeL}_{stat}_PLOT.png")
      plt.close()

for typeS in typeOfSorter:
  for stat in statusList:
    fig = plt.figure()
    fig.set_figwidth(12)
    i = 1
    for sizeL in sizeOfList:
      numpy_array_1 = np.array(data["BSPPI"][typeS][sizeL][stat])
      numpy_array_2 = np.array(data["BSWN"][typeS][sizeL][stat])
      numpy_array_3 = np.array(data["BSUNC"][typeS][sizeL][stat])
      s = SIZE[sizeL]
      c = COLOR[sizeL]
      cols = [numpy_array_1/s, numpy_array_2/s, numpy_array_3/s]
      bp = plt.boxplot(cols, positions=[i, i+3.5, i+7], widths=0.4)       
      plt.setp(bp['boxes'], color=c)
      i+=1
    ticks = [1, 2, 3, 4.5, 5.5, 6.5, 8, 9, 10]
    labels = []
    for algo in algorithms:
      for sizeL in sizeOfList:
        labels += [f"{algo}\n{sizeL}"]
    plt.ylabel("Time per item (ns)")
    plt.xticks(ticks, labels)
    plt.title(f"{typeS}, {stat}")
    plt.savefig(f"figures/{typeS}_{stat}_BOX.png")
    plt.close()
