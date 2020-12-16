# San_Joaquin_marine_life_predictor
Predicts the presence of aquatic micro-organisms in the San Joaquin Delta based on water quality measurements


## Project Hitsory/Workflow:

- Find USGS stations in the San Joaquin Delta region using the lat/lon bounding box feature on their site.

- Download the [`1972-2019PumpMatrix.xlsx` data from the California Dept of Fish and Wildlife](ftp://ftp.wildlife.ca.gov/IEP_Zooplankton/)

- Find the USGS stations with data including and prior to 2019.

- Scrape the data using `USGS_scraping.ipynb`

- Map USGS stations and pump stations using `visualizations/Plotly_map.ipynb`

- Match the pump stations to the USGS stations based on proximity and the distance up/downstream. Matchings can be found in `usgs_to_zooplankton_site` sheet in `usgs_locations_w_zoo_sites.xls`

- Take a _bell-shaped curve_ weighted moving average of the USGS data using an 11 day period with `EDA.ipynb` and `gauss.py`.

## File Directory

- The numbered notebooks located in `usgs` were used to read the usgs data for the corresponding station number and merge it with the zooplankton data for the appropriate hand-picked measurement stations. The resulting files were output to the `merged` directory