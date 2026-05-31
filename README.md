
# COVID-19 in Sweden
Analysis of COVID-19 pandemic in Sweden.

## repository structure
root/
│
├── data/
│ └── compact.csv #downlad by readme link!
│ └── expedinture.csv
│ └── infant_mortality.csv
│ └── testing.csv
│ └── vaccinations_age.csv

├── images/
│ ├── *all plots and images*
│
├── scripts/
│ ├── *all plot-generating scripts*
│
├── project.html # project report
├── README.md


## get data
Each data file (.csv) except for compact.csv is avaiable in the ./data directory. To download compact.csv [click here](https://docs.owid.io/projects/etl/api/covid/)


## run scripts

Each .py scripts generates a plot in /images directory. The plots are used in the [final report](./project.html)