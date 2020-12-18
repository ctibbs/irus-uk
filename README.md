# irus-uk
Code to extract and plot data from IRUS-UK (Institutional Repository Usage Statistics UK) via its two APIs. Further details on the IRUS-UK APIs is available at: https://irus.jisc.ac.uk/r5/uk/embed/api/

To use the IRUS-UK APIs, you will need a Requestor_ID - contact the [JISC helpdesk](mailto:help@jisc.ac.uk) with 'IRUS API' as the subject to request one. Both scripts have been set up to expect the Requestor_ID variable (py_local_settings.IRUS_Requestor_ID) to be imported from a local py_local_settings file. 

### Scripts
Both scripts are designed to run on a single IRUS-Uk repository. The chosen repository can be varied using the Platform parameter which corresponds to the JISC repository ID in the [IRUS-UK list of participants](https://irus.jisc.ac.uk/r5/uk/about/participants/#results_area).

irusuk_stats_r5_irus_pr.py - Python script to run the irus_pr IRUS-UK report. This can be used to extract and plot any of the available metric types for any of the item types e.g., to extract the total number of downloads for articles you would set Metric_Type=Total_Item_Requests and Item_Type=Article.

irusuk_stats_r5_pr.py - Python script to run the pr IRUS-UK report. This can be used to extract and plot any of the available metric types for all items in the repository e.g., to extract the total number of downloads for all items you would set Metric_Type=Total_Item_Requests.

