## SD Burrito Shops Analysis
______________________________________________________________


The goal of this project is to provide burrito lovers a tool they could use to search  burrito shops around San Diego county based on users' choice of criteria such as; shop rating, shop name, or type of burrito. The tool also provides visualizations of these shops on map plots which also allows the user to choose from a list of filling types and populates the maps absed on the users selection. We have also encorporated dashboards to allow users view the San Diego county burrito shops data from different angles. 

##### Visit our site using link:
_____________________________________________________________________

#### Finding Data & Cleanup
- Data was found on kaggle.com (https://www.kaggle.com/srcole/burritos-in-san-diego)
- we then cleaned up the data to remove unnecessary characters, Null values, added categories for a better usage of the data
- since our data did not contain Longitude & Latitude information, we used python's geocoder library to scrub this information from googleAPI for each of our shop entry

		```
        #create function for geo coding addresses
		def geomapper(address):
    		g = geocoder.google(address, key=geo_api_key)
    		lat = g.json['lat']
    		long = g.json['lng']
    		return (f'{lat},{long}')
        ```
- we then loaded our complete data onto SQLite DB
_________________________________________________________________________


#### Git Repo Contents 

###### DB Folder
- contains SQLite database and table 
###### Resources folder
- BurritoCleanLatLng.csv - csv file containing data with lng & lat (not needed to recreate project)
- Burrito_Clean_with_full_address.csv - raw data after clean up (not needed to recreate project)
###### Static
- **CSS** - contains CSS styling sheets
- **Images** - contains background images used for our pages
- **js** - contains files with JS codes for our plotting and visualization logic
###### Templates 
- contains each of our index.html pages we used for home page and plotting/visualization
###### app.py
- contains code for describing each of our /routes for our website
