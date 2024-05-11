# MLOps Project: Data Extraction

## Overview
This project extracts data from the homepages of Dawn and BBC news websites.

## Setup
- Install Python and create a virtual environment.
- Install required packages: `pip install requests beautifulsoup4`.

## Running the Scripts
Navigate to the `data_extraction` directory:
- Run `python extract_dawn.py` to extract data from Dawn.
- Run `python extract_bbc.py` to extract data from BBC.

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Data Transformation
This section explains how extracted data is cleaned and transformed into a structured JSON format. The script `transform_data.py` is used to clean text fields and standardize the data structure.

### Running the Transformation
The transformation functions are integrated into the extraction scripts. Run the extraction scripts as described above to process and view the transformed data.
