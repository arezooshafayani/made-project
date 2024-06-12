# Project Plan

## Title

<!-- Give your project a short title. -->

Analyzing the dominance of road transport in total energy consumption and its climate implications

## Main Question

<!-- Think about one main question you want to answer based on the data. -->

How does the energy consumption in road transport compare to the total energy consumption in the transport sector across different countries over the years, and what are the potential climate implications of this dominance?

## Description

<!-- Describe your data science project in max. 200 words. Consider writing about why and how you attempt it. -->

This project examines the significant role of road transport within the total energy consumption of the transport sector, leveraging data from two key datasets: "Final energy consumption in road transport by type of fuel" and "Final energy consumption in transport by type of fuel." The first dataset focuses on the energy used by various road vehicles, from cars to emergency vehicles, exclusively on public roads. The second broadens the scope to include all transport modes like rail, aviation, and navigation, excluding energy used at transport facilities.

By analyzing these datasets, the goal is to quantify how road transport's energy consumption compares across different countries over time and discuss the potential climate implications of its dominance. Through statistical techniques and visualizations, the project will outline energy usage trends, drawing connections to climate change impacts and suggesting targeted interventions. This approach offers insights into effective strategies for reducing the transport sector's environmental footprint, emphasizing the urgent need for sustainable transport policies.

## Datasources

<!-- Describe each datasources you plan to use in a section. Use the prefic "DatasourceX" where X is the id of the datasource. -->

### Datasource1: Final energy consumption in transport by type of fuel

- Metadata URL: https://ec.europa.eu/eurostat/databrowser/view/ten00126/default/table?lang=en&category=cli.cli_dri.cli_dri_tran
- Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ten00126/?format=SDMX-CSV&compressed=true
- Data Type: CSV

This dataset encompasses the total energy consumption across various transport modes including road, rail, domestic aviation, and navigation, while excluding international operations and non-transport energy uses. It provides a comprehensive view of energy use within national transport sectors, omitting energy consumption in airports, train stations, and ports, which is categorized under the service sector.

### Datasource2: Final energy consumption in road transport by type of fuel

- Metadata URL: https://ec.europa.eu/eurostat/databrowser/view/ten00127/default/table?lang=en&category=cli.cli_dri.cli_dri_tran
- Data URL: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/ten00127/?format=SDMX-CSV&compressed=true
- Data Type: CSV

This dataset details energy consumption specifically within road transport, covering vehicles like cars, buses, trucks, and emergency vehicles such as ambulances and fire trucks. It focuses on all forms of road transport, from urban to international journeys, across publicly accessible road networks, excluding off-road vehicle usage which is accounted for in other sectors like agriculture or construction.

## Work Packages

<!-- List of work packages ordered sequentially, each pointing to an issue with more details. -->

1. Search and Identify Two Datasets for Project [#1][i1]
2. build an automated data pipeline [#2][i2]
3. Build an automated data pipeline For Exercise 3 [#3][i3]
4. Create a report about your choice of data and how you improved it using an automated data pipeline in 3 Pages [#4][i4]
5. Add automated tests for my project [#5][i5]

[i1]: https://github.com/arezooshafayani/made-project/issues/1
[i2]: https://github.com/arezooshafayani/made-project/issues/2
[i3]: https://github.com/arezooshafayani/made-project/issues/3
[i4]: https://github.com/arezooshafayani/made-project/issues/4
[i5]: https://github.com/arezooshafayani/made-project/issues/5

