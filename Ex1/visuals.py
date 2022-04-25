import json 
import numpy as np
import matplotlib.pyplot as plt
import os

jj = open("output.json").read()

algorithms = ["BSPPI","BSUNC", "BSWN"]
typeOfSorter = ["INTEGER", "STRING", "DUMMY"]
sizeOfList = ["SMALL", "MEDIUM", "LARGE"]
statusList = ["RG", "AS", "SB"]

SIZE = {"SMALL": 10, "MEDIUM": 100, "LARGE": 1000}
COLOR = {"SMALL": 'r', "MEDIUM": 'g', "LARGE": 'b'}

data = json.loads(jj)

print(f"{'%-27s' % 'Instance variables'}: \
{'%-15s' % 'Minimum'} \
{'%-15s' % 'First quartile'} \
{'%-15s' % 'Median'} \
{'%-15s' % 'Third quartile'} \
{'%-15s' % 'Maximum'}")
print(f"{'-' * 102}")

if not os.path.exists("figures"):
  os.makedirs("figures")

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

      for algo in algorithms:
        arr = data[algo][typeS][sizeL][stat]
        print(f"{'%-7s' % typeS} {'%-3s' % stat} {'%-7s' % sizeL} {'%-7s' % algo}: \
{'%-15s' % np.min(arr)} \
{'%-15s' % np.quantile(arr, .25)} \
{'%-15s' % np.median(arr)} \
{'%-15s' % np.quantile(arr, .75)} \
{'%-15s' % np.max(arr)}")

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