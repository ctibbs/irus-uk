# irus-uk
Code to interact and extract data from IRUS-UK (Institutional Repository Usage Statistics UK) via the API. Further details on the IRUS-UK API is available at: https://irus.jisc.ac.uk/r5/uk/embed/api/

To use the IRUS-UK API, you will need a Requestor_ID - contact the [JISC helpdesk](mailto:help@jisc.ac.uk) with 'IRUS API' as the subject to request one.

irusuk_stats_r5_irus_pr.py - Python script to run the irus_pr IRUS-UK report. This can be used to extract any of the available metric types for any of the item types
e.g., to extract the total number of downloads for articles you would set Metric_Type=Total_Item_Requests and Item_Type=Article.

irusuk_stats_r5_pr.py - Python script to run the pr IRUS-UK report. This can be used to extract any of the available metric types for all items e.g., to extract the total number of downloads for all items you would set Metric_Type=Total_Item_Requests.

