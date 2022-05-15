from turtle import width
import pandas 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
dataframe = pandas.read_csv('web_app/public/final_data.csv')
dataframe["uid"] = np.char.mod('%d', dataframe["uid"])

df_correct = dataframe.query("correct")
df_no_outliers = dataframe.query("time <= 20000")
df_correct_no_outliers = df_correct.query("time <= 20000")

sns.histplot(data=df_no_outliers, x="time")
plt.title("Distribution of the times recorded (< 20s)")
plt.savefig('./figures/Figure_0.png')
plt.close()
sns.histplot(data=dataframe.query('csexp == "yes"'), x="uid", hue="correct", discrete=True, multiple="stack", palette={True:'green',False:'red'})
sns.histplot(data=dataframe.query('csexp == "no"'), x="uid", hue="correct", discrete=True, multiple="stack", palette={True:'lime',False:'red'})
plt.title("Correct and incorrect answers per participant (Green have CS experience)")
plt.savefig('./figures/Figure_1.png')
plt.close()
sns.set(rc={"figure.figsize":(20, 4)})
sns.histplot(data=dataframe, y="correctS", hue="correct", discrete=True, multiple="stack")
plt.title("Correct and incorrect answers per question")
plt.savefig('./figures/Figure_2.png')
plt.close()
sns.catplot(data=df_correct_no_outliers, x="uid", y="time", kind="box", showfliers = False)
plt.title("time taken per participant (Correct only, no outliers)")
plt.savefig('./figures/Figure_3.png')
sns.catplot(data=df_correct_no_outliers, x="style", y="time", kind="box", hue="csexp", showfliers = False)
plt.title("time taken per style (Correct only, no outliers)")
plt.savefig('./figures/Figure_4.png')
sns.catplot(data=df_correct_no_outliers, x="device", y="time", kind="box", hue="csexp", showfliers = False)
plt.title("time taken per device (Correct only, no outliers)")
plt.savefig('./figures/Figure_5.png')
sns.catplot(data=df_correct_no_outliers, y="correctS", x="time", kind="box", showfliers = True)
plt.title("time taken per question (Correct only, no outliers)")
plt.savefig('./figures/Figure_6.png')
sns.catplot(data=df_correct_no_outliers, x="correctI", y="time", kind="box", showfliers = False)
plt.title("time taken per correct index (Correct only, no outliers)")
plt.savefig('./figures/Figure_7.png')
sns.catplot(data=df_correct_no_outliers.query("csexp == 'yes'"), x="style", y="time", kind="box", hue="device", showfliers = False)
plt.title("time taken per style by people with CS experience (Correct only, no outliers)")
plt.savefig('./figures/Figure_8.png')
sns.catplot(data=df_correct_no_outliers.query("csexp == 'no'"), x="style", y="time", kind="box", hue="device", showfliers = False)
plt.title("time taken per style by people without CS experience (Correct only, no outliers)")
plt.savefig('./figures/Figure_9.png')

DEVICES = ["mouse", "trackpad", "touch"]
CASES = ["kebabcase", "camelcase"]
CSEXPS = ["yes", "no"]
CORRECTIS = ["== 0","!= 0","any"]

df_correct.loc[:,'time'] = np.round(df_correct.loc[:, 'time'])

print()
print(f"\
{'%-8s' % 'Device'} \
{'%-9s' % 'Style'} \
{'%-6s' % 'CSexp'} \
{'%-6s' % 'Index'} :      \
Minimum    \
First quartile            \
Median      \
Third quartile          \
Maximum             \
Mean               \
STD")
print(f"{'-' * 160}")
for device in DEVICES:
  for case in CASES:
    for csexp in CSEXPS:
      for correctI in CORRECTIS:
        query = f"device == '{device}' and style == '{case}' and csexp == '{csexp}'"
        if (correctI != 'any'):
          query += f'and correctI {correctI}'
        arr = df_correct.query(query)['time']
        print(f"{'%-8s' % device} {'%-9s' % case} {'%-6s' % csexp} {'%-6s' % correctI} : \
        {'%-9s' % np.min(arr)} \
        {'%-9s' % np.quantile(arr, .25)} \
        {'%-9s' % np.median(arr)} \
        {'%-9s' % np.quantile(arr, .75)} \
        {'%-9s' % np.max(arr)} \
        {'%-9s' % np.round(np.mean(arr),3)} \
        {'%-9s' % np.round(np.std(arr),3)}"
        )
df_csexp = dataframe.query("csexp == 'yes'")
mu = np.mean(df_csexp["time"])
std = np.std(df_csexp["time"])
sqN = np.sqrt(len(df_csexp))
print("With CS experience:")
print(f"Mean = {mu}")
print(f"STD = {std}")
print(f"sqN = {sqN}")
df_no_csexp = dataframe.query("csexp == 'no'")
mu_n = np.mean(df_no_csexp["time"])
print("Without CS experience:")
print(f"Mean = {mu_n}")
z = (mu_n - mu)/(std / sqN)
print(f"Z-score H_1 = {z}")
