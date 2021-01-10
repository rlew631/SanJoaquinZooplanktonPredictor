# San Joaquin Marine Micro-Organism Predictor
The purpose of this project is to predict the presence of aquatic micro-organisms in the San Joaquin Delta based on water quality measurements from USGS. These organisms are a key food source for the endangered Delta Smelt which has experienced a rapid population decline in the last few years.

## Project History/Workflow:

- Find USGS stations in the San Joaquin Delta region using the lat/lon bounding box feature on their site.
- Download the [`1972-2019PumpMatrix.xlsx` data from the California Dept of Fish and Wildlife](ftp://ftp.wildlife.ca.gov/IEP_Zooplankton/)
- Find the USGS stations with data including and prior to 2019.
- Scrape the data using `scrape_then_merge.py`
- Map USGS stations and pump stations using `visualizations/Plotly_map.ipynb`
- Match the pump stations to the USGS stations based on proximity and the distance up/downstream. Matchings can be found in `usgs_to_zooplankton_site` sheet in `usgs_locations_w_zoo_sites.xls`
- Take a _bell-curve_ weighted moving average of the USGS data using an 11 day period with `EDA.ipynb` and `gauss.py`. This resulted in the bell curve weights being centered on day 6 and seemed to offer the best correllation between the various water quality metrics and the amount of zooplankton present in the pump stations.
- Create a model which predicts the amount of zooplankton present in the water based on the weighted moving average water quality metrics.

## Creating the Model:
After comparing the various water quality metrics to the presence of the various zooplanktons it was clear that the samples fell under a bell curve distribution. This makes sense as the organisms would do best in a certain pH, temperature or salinity range and there would be a decreased in observed zooplankton if these metrics fell outside of the goldilocks zone. This meant there was some final feature engineering to create something closer to a linear relationship with the recorded zooplankton observations. The `FinalModel.ipynb` file works through this final feature engineering and several other aspects of the modelling process. This process involved:

- Fitting a bell curve to the water quality metrics to find the peak which represented the ideal range.
- Creating an intermediate feature which is the absolute distance from that ideal value
- Performing a log transformation on that intermediate feature
- using a linear model to correlate the log transformed feature with the presence of zooplankton

<!--
put a drawio diagram here
-->
## File Directory

- The numbered notebooks located in `usgs` were used to read the usgs data for the corresponding station number and merge it with the zooplankton data for the appropriate hand-picked measurement stations. The resulting files were output to the `merged` directory
