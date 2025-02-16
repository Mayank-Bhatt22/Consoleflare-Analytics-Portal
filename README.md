# Consoleflare-Analytics-Portal
This Streamlit app provides an intuitive data analytics portal for exploring CSV and Excel files. Users can upload datasets, view summaries, check data types, inspect top/bottom rows, and analyze value counts. It also offers group-by operations with dynamic visualizations, including bar, line, scatter, pie, and sunburst charts using Plotly.
# Consoleflare Analytics Portal

## Overview

Consoleflare Analytics Portal is a user-friendly Streamlit application designed for quick and efficient data exploration and visualization. The portal enables users to upload CSV or Excel files, analyze their contents, and generate interactive charts using Plotly.

## Features

- **File Upload:** Supports CSV and Excel file formats.
- **Data Display:** Shows the dataset in a structured format with interactive components.
- **Dataset Summary:** View dataset dimensions, statistical summaries, and data types.
- **Top & Bottom Rows:** Easily navigate through the dataset with adjustable row previews.
- **Value Counts:** Perform frequency analysis of categorical columns with visualizations.
- **GroupBy Analysis:** Summarize data using aggregation functions like mean, sum, count, min, and max.
- **Data Visualization:** Create bar, line, scatter, pie, and sunburst charts for deeper insights.

## Installation

Ensure you have Python installed, then set up the required dependencies:

```sh
pip install pandas plotly streamlit openpyxl
```

## Usage

1. Run the application using Streamlit:
   ```sh
   streamlit run app.py
   ```
2. Upload a CSV or Excel file.
3. Explore dataset details, perform aggregations, and visualize trends.

## Requirements

- Python 3.7+
- Required Libraries:
  - `streamlit`
  - `pandas`
  - `plotly`
  - `openpyxl` (for Excel files)

## How It Works

### File Upload

- Drag and drop a CSV or Excel file into the uploader.
- The dataset is displayed instantly.

### Dataset Summary

- Get an overview of dataset dimensions.
- View statistical summaries of numerical data.
- Inspect column data types and names.

### Value Counts Analysis

- Select a column to see the frequency of unique values.
- View bar, line, and pie chart visualizations.

### GroupBy Analysis

- Choose columns to group data.
- Select an aggregation function (mean, sum, count, min, max).
- View results in a table and generate visualizations.

### Data Visualization

- Generate various charts:
  - **Bar Chart**: Compare values across categories.
  - **Line Chart**: Show trends over time.
  - **Scatter Plot**: Visualize relationships between numerical columns.
  - **Pie Chart**: Show proportions of categorical values.
  - **Sunburst Chart**: Display hierarchical data structures.

## Troubleshooting

- **Encoding Issues?** Try opening the file in a text editor and ensuring it’s UTF-8 encoded.
- **Missing Libraries?** Run `pip install -r requirements.txt` to install all dependencies.
- **Graph Not Displaying?** Ensure the selected columns contain numerical values where needed.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## License

This project is open-source and available under the MIT License.
