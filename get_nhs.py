import urllib.request
#for ccg coordinates https://openprescribing.net/api/1.0/org_location/?q=05Q&format=json
#for getting info on all ccg counties 'https://openprescribing.net/api/1.0/org_location/?org_type=ccg&format=json'
#for getting info an all spending https://openprescribing.net/api/1.0/spending_by_ccg/?code=03&format=json
import json
import matplotlib.dates
import datetime
import matplotlib.pyplot as plt
import pandas as pd

names = [("Gastro-Intestinal System","01"),("Cardiovascular System","02"),("Respiratory System", "03"),("Central Nervous System","04"),("Infections","05"),("Endocrine System","06")]
all_dates={}
all_costs = {}

for name,code in names:
    url = 'https://openprescribing.net/api/1.0/spending_by_ccg/?code=%s&format=json'%code
    fileobj = urllib.request.urlopen(url)
    all_data = json.loads(fileobj.read().decode('utf-8'))
    cost_by_date = {}
    for entry in all_data:
        if not  entry["date"] in cost_by_date:
            cost_by_date[entry["date"]]=0.0
        cost_by_date[entry["date"]]+=entry["actual_cost"]
    all_dates[name] = [datetime.datetime.strptime(d,'%Y-%m-%d') for d,_ in cost_by_date.items()]
    all_costs[name] = [c for _,c in cost_by_date.items()]

plt.style.use('seaborn-darkgrid')
palette = plt.get_cmap('Set1')

rule = matplotlib.dates.rrulewrapper(matplotlib.dates.MONTHLY, interval=4)
loc = matplotlib.dates.RRuleLocator(rule)
formatter = matplotlib.dates.DateFormatter("%d %m %y")
fig,ax = plt.subplots()
n = 0
for name,_ in names:
    n+=1
    plt.plot_date(all_dates[name],all_costs[name], color=palette(n), linewidth=1, label=name)

ax.xaxis.set_major_locator(loc)
ax.xaxis.set_major_formatter(formatter)
ax.xaxis.set_tick_params(rotation=30, labelsize=10)
plt.legend(loc=2)
plt.title("Perscription costs over time")
plt.xlabel("Time")
plt.ylabel("Actual cost")
plt.show()
