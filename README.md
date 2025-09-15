# Pharma Pulse

Pharma Pulse is a web-based analytics dashboard and chatbot platform for pharmaceutical sales data. It provides interactive visualizations, drug information, predictive analytics, and a conversational assistant for insights.

## Features

- **Dashboard:** Embedded Power BI for sales visualization.
- **Drug Information:** Detailed cards for major drug categories and examples.
- **Forecasting:** Auto ARIMA-based predictions for daily and weekly drug sales.
- **Chatbot:** Integrated Botpress chatbot for real-time insights.
- **Research & Details:** Pages for dataset overview, architecture, and drug research.

## Project Structure

```
.
├── app.py
├── modelapp.py
├── README.md
├── models/
│   ├── auto_arima_model_daily_M01AB.pkl
│   ├── auto_arima_model_daily_M01AE.pkl
│   ├── auto_arima_model_daily_N02BA.pkl
│   ├── auto_arima_model_daily_N02BE.pkl
│   ├── auto_arima_model_daily_N05B.pkl
│   ├── auto_arima_model_daily_N05C.pkl
│   ├── ...
├── static/
│   ├── main.js
│   └── css/
│       └── style.css
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── drug.html
│   ├── aboutus.html
│   ├── forecasting.html
│   ├── predictions.html
│   ├── prediction2.html
│   ├── detail.html
│   ├── xsearch.html
│   ├── xmo1ab.html
│   ├── xmo1ae.html
│   ├── xno2ba.html
│   ├── xno2be.html
│   ├── xno5b.html
│   ├── xno5c.html
│   ├── xdrugs.html
│   ├── xchatbot.html
│   ├── xdetails.html
│   └── xstatistics.html
```

## Getting Started

1. **Install dependencies:**
   ```sh
   pip install flask pandas
   ```

2. **Run the app:**
   ```sh
   python app.py
   ```
   or
   ```sh
   python modelapp.py
   ```

3. **Access the site:**  
   Open [http://localhost:5004](http://localhost:5004) in your browser.

## Requirements

- Python 3.x
- Flask
- pandas
- Pre-trained ARIMA models in the `models/` directory

## Usage

- Navigate through the dashboard, drug info, forecasting, and chatbot via the navigation bar.
- Use the prediction tool to forecast drug sales by date or week.
- Explore research and details pages for more information about the dataset and architecture.

## License

This project is for educational and demonstration purposes.