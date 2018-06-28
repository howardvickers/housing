# housing
## Housing: Looking at Property Market with Data Science
#### Text here.

### Overview & Purpose				
The goal of this project is to ...

### Data Sources
All data are available online as public records, either by county or otherwise geo-located.  The data include:
* Property prices:
  * Zillow: [data.chhs.ca.gov](https://data.chhs.ca.gov/dataset/asthma-ed-visit-rates-lghc-indicator-07)
* Socio-economic data:  [countyhealthrankings.org](http://www.countyhealthrankings.org/rankings/data)
* Air quality data: [epa.gov](https://aqs.epa.gov/aqsweb/airdata/download_files.html)
* FIPS codes: [census.gov](https://www.census.gov/2010census/xls/fips_codes_website.xls)

Data was selected nationally:

### Data Challenges
Text here


### Models
Text here
| Model                           | RMSE (Train)         | RMSE (Test)      | R Squared     |
| ------------------------------- |---------------| --------------| --------------|
| Linear Regression               | 11.02          | 12.59          |  0.76        |
| Elastic Net (a=1, l1=0.9)     | 11.87           | 12.01          |  0.78        |
| Random Forest                   | 7.09          | 10.80          |    0.82      |
| Gradient Boosting               | 2.00          | 10.68          | 0.82         |
| Support Vector Regressor      | 11.24          | 12.69          |  0.75        |
| KNN Regressor                | 0.03          | 11.49          |    0.80      |


### Features
Text here

### Code
The code is structured as follows:
* [data.py](https://github.com/howardvickers/housing/blob/master/src/data.py) imports data from various csv files (downloaded from above-mentioned sources) and returns a single pandas dataframe.  The resulting dataset is also stored as a csv file to enable faster loading of data on future occasions.  The code includes functionality to run the model with selected states.
* [data_processing.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/data_processing.py) imports data from data.py and processes it for feature selection and for use in the algorithms.  
* [ols_model_hot_one.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/ols_model_hot_one.py) runs (trains and predicts) the OLS model.
* [get_feat_imps.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/get_feat_imps.py) runs the random forest model to generate the feature importances for the feature importances chart.
* [comparison.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/comparison.py) allows a comparison of models and their results.
* [get_results.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/get_results.py) processes data from the web app and returns results for representation as html in the web app.
* [charts.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/charts.py) generates the feature importances chart.
* [state_color_map.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/state_color_map.py) generates the state map-chart according to predictions based on policy changes input via the web app.
* [app.py](https://github.com/howardvickers/galvanize-capstone-asthma/blob/master/src/app.py) serves the HTML and related files for the web app, drawing upon the above data and model files.

The code is available at [github.com/howardvickers](https://github.com/howardvickers).

### Web App
Decide web app or jupyter notebook.


### Results
Text here

### References
Text here
