We developed a 1km resolution long-term soil moisture dataset of China derived through machine learning trained with in-situ measurements of 1,789 stations, named as SMCI1.0(Soil moisture of China based on In-situ data, Li et al, 2022). SMCI1.0 provides 10-layer soil moisture with 10 cm intervals up to 100 cm deep at daily resolution over the period 2010-2020. Random Forest is used to predict soil moisture using ERA5-land time series, leaf area index, land cover type, topography and soil properties as covariates. Using in-situ soil moisture as the benchmark, two independent experiments are conducted to investigate the estimation accuracy of the SMCI1.0: year-to-year experiment (ubRMSE ranges from 0.041-0.052 and R ranges from 0.883-0.919) and station-to-station experiment (ubRMSE ranges from 0.045-0.051 and R ranges from 0.866-0.893). As SMCI1.0 is based on in-situ data, it can be useful complements of existing model-based and satellite-based datasets for various hydrological, meteorological, and ecological analyses and modeling, especially for those applications requiring high resolution SM maps.

Temporal Coverage	2010 - 2020, Daily
Depth Coverage	10-layer soil moisture with 10 cm intervals up to 100 cm 
Projection	Sinusoidal / Geographic Coordinates
Resolution	~1 kilometer (30 arc seconds）
Spatial Coverage	China,1km (4320×7560 rows/columns) ,73° - 136°E and 18°-54° N
Data Format	NetCDF4(.nc)
Units	0.001m³/m³
Filled Value	-999


Temporal Coverage	2010 - 2020, Daily
Depth Coverage	10-layer soil moisture with 10 cm intervals up to 100 cm 
Projection	Sinusoidal / Geographic Coordinates
Resolution	~9 kilometer（0.1 degree）
Spatial Coverage	China, ~9km (360×630 rows/columns）,73° - 135.9°E and 18.1°- 54°N
Data Format	NetCDF4 (.nc)
Units	0.001 m³/m³
Filled Value	-999
