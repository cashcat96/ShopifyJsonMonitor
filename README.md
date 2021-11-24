# ShopifyJsonMonitor
A simple set of scripts which enable the monitoring of the products.json file for any web store that utilizes Shopify

## To get the json website monitor up and running, do the following:
- Edit runscripts.sh
  - add directory
- Edit notify.sh
  - enter the alert name and add in any notification agents
- Edit productpuller_new.py
  - edit the order and naming of the things in the json file (option1, option2, etc.)
  - edit the website base url at the bottom of the file
- Edit compareproduct.py
  - edit the notification diction with the changes made to the things in the json file
  - you may want to remove some values from the notification string if nothing has a color or size etc.
- add runscripts.sh to crontab
