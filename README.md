# CWD County-based Prediction Web App

## Overview
This repository contains the code for a web application designed to predict Chronic Wasting Disease (CWD) status in counties based on environmental, geographical and human factors. The application is built using Streamlit and utilizes a Random Forest model trained on relevant features to perform the prediction.

## Features
- **CWD Prediction**: Predicts whether a county is likely to be CWD positive or negative based on user input.
- **Interactive UI**: Easy-to-use sliders and select boxes for inputting data.
- **Immediate Results**: Instantly displays CWD status prediction upon user request.

## Prerequisites
Before running this application, you need the following installed:
- Python 3.6+
- streamlit
- numpy
- Pillow



## Usage
The application has a simple interface where the user can input the following parameters:
- Number of Cervid Facilities
- Total Harvest
- Hunting Enclosures
- Baiting
- Feeding
- Whole Carcass Import
- Urine Lures
- Captive Status
- Forest (Average Proportion)
- Clay (Average Percent)
- Streams (Average distance to the nearest water)

After inputting the data, the user can click the 'CWD Test Result' button to receive a prediction.

## Model Information
The model used in this application is a Random Forest Classifier, which has been trained and serialized as 'rf_model2.pkl'. Upon starting the app, the model is loaded, and it is used to make predictions based on the user's input.

## Visualization
Upon prediction, an image will be displayed to indicate a positive or negative result:
- A positive prediction displays 'deerp.png'.
- A negative prediction displays 'deern.png'.

Additionally, the app includes a banner image 'CWD1.png' to enhance the user interface.

## License
This project is open source and available under the [MIT License](LICENSE).

## Contributions
Contributions to this project are Multistate Conversation Grant # F23AP00488-00.

## Acknowledgments
Thanks to all contributors and researchers in the field of wildlife disease management whose work supported the development of this application.

## Contact
For support or to report issues, please file an issue on the GitHub issue tracker for this repository.
