# Exercise Badges

![](https://byob.yarr.is/arezooshafayani/made-project/score_ex1) ![](https://byob.yarr.is/arezooshafayani/made-project/score_ex2) ![](https://byob.yarr.is/arezooshafayani/made-project/score_ex3) ![](https://byob.yarr.is/arezooshafayani/made-project/score_ex4) ![](https://byob.yarr.is/arezooshafayani/made-project/score_ex5)

# Analyzing the dominance of road transport in total energy consumption and its climate implications

![road transport](project/Images/MainImg.jpg)
Reference: Photo by [Unsplash](https://unsplash.com/photos/aerial-view-of-highway-full-of-cars-and-trucks-traffic-jam-in-the-middle-of-green-forest-netherlands-M1GDoN_YPaU)

## Introduction

The transportation sector is a major contributor to global energy consumption and greenhouse gas emissions. Within this sector, road transport stands out due to its extensive use of fossil fuels and its impact on climate change. This report investigates the dominance of road transport in the overall energy consumption of the transport sector across different countries over the years, using two key datasets. The aim is to quantify road transport's energy consumption relative to total transport energy consumption and discuss the potential climate implications of this dominance.

## Data sources

### Data Source1: Final energy consumption in transport by type of fuel

- Metadata URL: https://ec.europa.eu/eurostat/databrowser/view/ten00126/default/table?lang=en&category=cli.cli_dri.cli_dri_tran
- Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ten00126/?format=SDMX-CSV&compressed=true
- Data Type: CSV
- Period: 2011 to 2022
- Description: This dataset provides a comprehensive view of energy consumption across various transport modes, including road, rail, domestic aviation, and navigation, while excluding international operations and non-transport energy uses.

### Datasource2: Final energy consumption in road transport by type of fuel

- Metadata URL: https://ec.europa.eu/eurostat/databrowser/view/ten00127/default/table?lang=en&category=cli.cli_dri.cli_dri_tran
- Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ten00127/?format=SDMX-CSV&compressed=true
- Data Type: CSV
- Period: 2011 to 2022
- Description: This dataset focuses on energy consumption within road transport, covering vehicles like cars, buses, trucks, and emergency vehicles on public roads.

## Analysis and Conclusion

The analysis reveals that road transport consistently accounts for a significant portion of total transport energy consumption across various countries, particularly in Germany, France, and Italy. This dominance has profound climate implications due to the heavy reliance on fossil fuels like motor gasoline and diesel oil, which are major sources of greenhouse gas emissions. The trends from 2011 to 2022 show a strong correlation between total and road transport energy use, with notable peaks around 2017-2018 and a sharp decline in 2020, likely due to the COVID-19 pandemic. This underscores the urgent need for targeted policies to reduce emissions by transitioning to cleaner energy sources, improving fuel efficiency, and promoting alternative transport modes. However, the analysis is limited by the scope of available data and does not account for all factors influencing energy consumption, suggesting the need for further research to fully understand and address the transport sector's impact on climate change.

## Jupyter notebook report

A Jupyter notebook report named [analysis-report.ipynb](https://github.com/arezooshafayani/made-project/tree/main/project/analysis-report.ipynb) is available in the `project` directory or the [analysis-report.pdf](https://github.com/arezooshafayani/made-project/tree/main/project/analysis-report.pdf).

## Run Pipeline Locally

1. Clone the project

`bash`
git clone https://github.com/arezooshafayani/made-project.git

````````

2. In the project directory

```````bash```````
  cd made-project
````````

3. Run the bash script `project/pipeline.sh`

`bash`
./project/pipeline.sh

````````

This will run the Pipeline and create a SQL database in `\data` directory, DB name is `energy_consumption.db`.

## Running Tests

To run tests, run the following command

```````bash```````
  ./project/tests.sh
````````
