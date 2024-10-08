﻿# Shark Attack Analysis Project
<p align="center">
<img src="tiburon.gif" alt="Tiburon con hambre">
</p>

## Team Members

| Name             | LinkedIn Profile | Brief Description |
|------------------|------------------|-------------------|
| Almudena Martín Castro         | https://www.linkedin.com/in/almudenamcastro/      |  Science communicator and data enthusiast |
| Danny David Rodas Galarza         | https://www.linkedin.com/in/dannyrodasgalarza/     | Developer and Data Analyst |
| Luis Humberto Rodríguez Fuentes        | https://www.linkedin.com/in/luis-h-rodr%C3%ADguez-fuentes/     | Data Analyst |
| Adrián Benítez Rueda       | https://www.linkedin.com/in/adri%C3%A1n-ben%C3%ADtez-rueda-10102565/?originalSubdomain=es    | Data Analyst |

## Project Overview

### Business Problem

We are an environmental agency with the mission of raising awareness about climate change and wildlife preservation. Recently, we have identified an opportunity to inform the public about an emerging concern: shark attacks. While shark attacks have historically been a rare phenomenon, there is evidence to suggest that climate change is contributing to an increase in their frequency and intensity.

Our campaign aims to address this issue by:

- Informing the public about how climate change has contributed to the rise in shark attacks around the world.
- Educating people on how to minimize the risk of shark attacks.
- Highlighting the regions most affected by this phenomenon.

### Initial Hypotheses

1. **Climate Change Impact**: We hypothesize that climate change has increased the number of shark attacks globally.
2. **Geographical Hotspots**: We believe that warmer areas of the planet are more likely to experience shark attacks due to changing water temperatures and shifting ecosystems.
3. **Human Influence**: We suspect that certain human activities (e.g., water sports, fishing, pollution) might correlate with an increase in shark attacks.

### Required Data

To validate or refute our hypotheses, we will gather and analyze the following data:

- **Number of shark attacks**: Historical data on the number of recorded shark attacks over the years.
- **Date**: Temporal data to observe trends over time.
- **Location**: Geographic data to determine where attacks are most prevalent.
- **Activity**: Information on the activities that victims were engaged in during the attacks to assess human influence.

## Data Sources

- Shark Attack Database: [\[Link to source\]](https://www.sharkattackfile.net/spreadsheets/GSAF5.xls)
- Presentación: [\[Link to source\]](https://docs.google.com/presentation/d/1TY9rHeRTEyUmi2aREjad6TL2w9h_PQFI1FtsjYlKhEA/edit?usp=sharing)

## Methodology

1. **Bussiness problem and hypothesis definition**: Define the business problem and the data we need to test our hypothesis. 
2. **Data Cleaning**: Processing the raw data to handle missing values, remove duplicates, and correct errors.
3. **Exploratory Data Analysis (EDA)**: Understanding the distribution of data, detecting trends, and identifying correlations between variables.
4. **Hypothesis Testing**: Using statistical techniques to test our initial assumptions and draw meaningful conclusions from the data.
5. **Visualization**: Presenting the findings through informative visualizations such as heat maps, bar charts, and geographical maps.

## Results

This section will include key findings and insights drawn from the analysis. For now, placeholders are provided for future updates:

1. **Finding 1**: since the 90s the attacks have increased, since 2007 the average has not dropped below 100, since 1995 global temperatures have started to rise.
2. **Finding 2**: Most of the attacks were carried out in the United States and Australia.


## Tools and Technologies

- **Programming Language**: Python
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, 
- **Visualization**: Plotly
- **Version Control**: Git
- **Data Storage**: CSV, xlsx.

## How to Use

To replicate or build upon this analysis, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/cohet3/sharkAtack_g7.git
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
3. Run the analysis scripts in the src/ directory
     ```bash
   python src/main.ipynb


## Future Work
Advanced Modeling: Explore machine learning models to predict future trends in shark attacks based on environmental factors.
Public Awareness Campaign: Build interactive tools or dashboards to engage the public with our findings.
Further Data Collection: Include more granular data, such as water temperatures, sea currents, and migration patterns of sharks.
## Conclusion
This project serves as an effort to understand the potential impacts of climate change on shark behavior and the risks to human life. By analyzing real-world data, we aim to provide actionable insights that can both educate the public and inform environmental policy decisions.
