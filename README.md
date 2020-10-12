# San_Joaquin_marine_life_predictor
Predicts the presence of aquatic micro-organisms in the San Joaquin Delta based on water quality measurements


## Project History/Workflow: A.K.A. How to reproduce the results

- Find USGS stations in the San Joaquin Delta region using the lat/lon bounding box feature on their site.

- Download the `1972-2019PumpMatrix.xlsx` data from the California Dept of Fish and Wildlife: ftp://ftp.wildlife.ca.gov/IEP_Zooplankton/

- Find the USGS stations with data including and prior to 2019.

- Scrape the data using `USGS_scraping.ipynb` (initially just the San Joaquin R A Jersey Point CA USGS data was used). (note to self: upload most recent version!)

- Load the `usgs.csv` file and create new columns which are a gaussian weighted average of the data over an 11 day period. This is done using `EDA.ipynb` and `gauss.py`. 11 days was chosen as it produced the clearest relationship between the features and targets (water quality factors and measured zooplankton population) when comparing pairplots.

- Map USGS station and pump station locations using `visualizations/Plotly_map.ipynb`

- Match the pump stations to the USGS stations based on proximity and the distance up/downstream. Matchings can be found in `usgs_to_zooplankton_site` sheet in `usgs_locations_w_zoo_sites.xls`

- Run the 11337190, 11455478, 11455508 and 380631122032201 notebooks to merge the usgs station data with the zooplankton samples from the appropriate locations.

- Run `merged/merger.ipynb` to combine the 4 dataframes from the previous step.

- Run `feature_transform.ipynb` to take the modally distributed data, fit a bell curve to it and express it as a logarithmic function of the distance the given feature is from the "goldilocks zone" to produce high quantities of zooplankton. (see the notebook or `visualizations/feature_subplots.png` for details)

- Run lin_reg.ipynb to generate a regular linear regression model, lasso linear regression model and ridge regression model.

- View pdf for summary
