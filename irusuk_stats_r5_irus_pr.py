##Script to extract and plot publication statistics from IRUS-UK release 5 IRUS_PR report
##
##Parameters that can be selected by the user: BeginDate, EndDate, Item_Type, Metric_Type, Platform, and Granularity
##
##Usage: >python irusuk_stats_r5_irus_pr.py Item_Type=Dataset Metric_Type=Total_Item_Requests
##BeginDate=2020-01 EndDate=2020-10 Platform=8 Granularity=month
##
##
##Written by C. Tibbs (Dec 2020)
##

##Import Python packages
import matplotlib.pyplot as plt
import requests
import json
import datetime
import calendar
import sys
from http import HTTPStatus
import py_local_settings

##Evaluate variables passed in call
var_dict = {}
for user_input in sys.argv[1:]:
    if '=' not in user_input:
        continue
    var_name = user_input.split('=')[0]
    var_value = user_input.split('=')[1]
    var_dict[var_name] = var_value

##Define parameters
if 'Item_Type' in var_dict:
    Item_Type = var_dict['Item_Type']
else:
    Item_Type = 'Dataset'
if 'Metric_Type' in var_dict:
    Metric_Type = var_dict['Metric_Type']
else:
    Metric_Type = 'Total_Item_Requests'    
if 'BeginDate' in var_dict:
    BeginDate = var_dict['BeginDate']
else:
    BeginDate = '2020-01'
if 'EndDate' in var_dict:
    EndDate = var_dict['EndDate']
else:
    EndDate = '2020-10'    
if 'Platform' in var_dict:
    Platform = var_dict['Platform']
else:
    Platform = 8
if 'Granularity' in var_dict:
    Granularity = var_dict['Granularity']
else:
    Granularity = 'month' 
Release = 5
Report = 'irus_pr'
Requestor_ID = py_local_settings.IRUS_Requestor_ID
Attributes = 'Irus:Item_Type'
download_stats = {}

##Define the IRUS-UK API parameters
url = 'https://irus.jisc.ac.uk/sushiservice/irus/reports/'+Report
params = {'requestor_id': Requestor_ID, 'platform': Platform, \
          'begin_date': BeginDate, 'end_date': EndDate, \
          'irus:item_type': Item_Type, 'attributes_to_show': Attributes, \
          'granularity': Granularity, 'metric_type': Metric_Type}

##Call the IRUS-UK API
r = requests.get(url, params=params)

##Check if API call was unsuccessful
if r.status_code != HTTPStatus.OK:
    print('Problem with this call of the IRUS-UK API...')

##Check if API call was successful
elif r.status_code == HTTPStatus.OK:
    ##Save data
    irus_data = json.loads(r.text)

    ##Print the report headers
    print('')
    print('#'*50)
    print(irus_data['Report_Header']['Report_ID']+' - '+irus_data['Report_Header']['Report_Name'])

    ##Loop over all of the different item types   
    for item in irus_data['Report_Items']:

        ##Print platform and item type
        print(item['Platform']+' - '+item['Irus:Item_Type'])
        print('')

        ##Loop over the periods of interest for the selected item type
        for period in item['Performance']:

            ##Extract periods
            begin_date_str = period['Period']['Begin_Date']
            begin_date = datetime.datetime.strptime(begin_date_str, '%Y-%m-%d')
            end_date_str = period['Period']['End_Date']
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d')

            ##Print periods
            print(begin_date_str+' - '+end_date_str)
                                
            ##Loop over the metric types
            for metric in period['Instance']:

                ##Only extract stats for selected metric type
                if metric['Metric_Type'] == Metric_Type:
                    count_str = metric['Count']
                    count = int(count_str)

                    ##Print stats
                    print('\t',metric['Metric_Type'],'=', metric['Count'])

                    ##Collate stats into dictionary
                    download_stats[calendar.month_name[begin_date.month]+' '+str(begin_date.year)] = count

    print('')
    print('#'*50)

##Plot stats
fig = plt.figure()
plt.bar(range(len(download_stats)), list(download_stats.values()), align='center')
plt.xticks(range(len(download_stats)), list(download_stats.keys()), rotation=90, fontsize=6)
plt.grid(b=True, which='major', axis='y', linestyle='dashed', zorder=0)
plt.title(item['Platform']+': '+Item_Type)
plt.ylabel(Metric_Type)
plt.subplots_adjust(bottom=0.20)
plt.savefig(Metric_Type+'_'+Item_Type+'_'+Report+'.pdf')

    
