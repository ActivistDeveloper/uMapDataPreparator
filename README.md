# uMapDataPreparator

## Purpose
This python script can be used to simplify enriching and converting csv data containing information about houses owned by the real estate company called Heimstaden into a geojson format so that this data can be imported into a specifically prepared umap hosted at umap.openstreetmap.com

## How to use
### Preperation
The script needs the following additional packagages for execution:
- pandas
- requests

Install them (preferably in a [virtual environment](https://docs.python.org/3/library/venv.html)) before executing the script ParseCSVToGeoJSON.py.

### Usage
For exectuting the script run it via the following command:

```
python3 ParseCSVToGeoJSON.py
```

If you run the script without an additional parameter it expects to find a file called "Neue-Heimstaden-Häuser-für-die-Karte.csv" at the same location as the script.

By executing the previous command with an additional paramter an other location for the expected file can be specified.

##### Neue-Heimstaden-Häuser-für-die-Karte.csv
The previously mentioned file at this or another given location is expected to  be a .csv where the first row has the following structure:

|name|Bezirk|Stadtteil|Millieuschutzgebiet|Objektnummer|Abgeschlossenheitsbescheinigung|Abwendungsvereinbarung|Kaufdatum|Vorbesitzerin|Umwandlungserlaubnis|Wohnungen|Gewerbeeinheiten|Kaufdatum Akelius|Unterfirma|Notizen|Layer|
|----|------|---------|-------------------|------------|-------------------------------|----------------------|---------|-------------|--------------------|---------|----------------|-----------------|----------|-------|-----| 

For now only these rows will be processed, where the value of column Layer is "ohne Akelius"


