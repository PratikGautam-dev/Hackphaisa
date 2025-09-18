# KrishiAI - Smart Farming Assistant

An AI-powered farming assistant that helps farmers make data-driven decisions about crop selection and management.

## Features
- Crop recommendation based on location and environmental factors
- Weather forecast integration
- Market price analysis
- Detailed crop analysis with visualizations
- Interactive map interface

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create .env file with required API keys:
```
OPENWEATHER_API_KEY=your_key_here
GEMINI_API_KEY=your_key_here
```

3. Start the application:
- Double click `start_servers.bat` 
OR
- Run these commands in separate terminals:
```bash
# Terminal 1 - Backend
cd backend
uvicorn main:app --reload --port 8000

# Terminal 2 - Frontend
cd project-env
streamlit run streamlit_app.py
```

4. Access the application:
- Frontend: http://localhost:8501
- Backend API: http://localhost:8000/docs

## Environment Variables

The following environment variables are required:

- `OPENWEATHER_API_KEY`: Get from [OpenWeather](https://openweathermap.org/api)

## Development Setup

For development, you might want to install additional packages:

```bash
pip install -r requirements-dev.txt  # For development dependencies
```

# Agricultural Commodity Price Analysis System

A comprehensive data analysis system for tracking and analyzing agricultural commodity prices across various states and districts in India. The dataset contains daily price information for different agricultural commodities including fruits, vegetables, cereals, and spices.

## Features

- **Extensive Coverage**: Data from multiple states and districts across India
- **Detailed Price Information**: Includes minimum, maximum, and modal prices
- **Multiple Commodity Categories**: 
  - Fruits (e.g., Apples, Bananas, Mangoes)
  - Vegetables (e.g., Onions, Tomatoes, Potatoes)
  - Cereals and Pulses
  - Spices and Condiments
  
## Data Structure

The dataset includes the following information:
- State
- District
- Market
- Commodity
- Variety
- Grade
- Arrival Date
- Minimum Price
- Maximum Price
- Modal Price

## Installation Requirements

1. Python 3.7 or higher
2. Required Python packages:
   ```bash
   pip install pandas
   pip install numpy
   pip install matplotlib
   pip install seaborn
   ```

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/agri-price-analysis.git
   ```

2. Navigate to the project directory:
   ```bash
   cd agri-price-analysis
   ```

3. Run the analysis scripts:
   ```bash
   python analyze_prices.py
   ```

## Data Analysis Capabilities

1. **Price Trends**
   - Track commodity price variations over time
   - Analyze seasonal price patterns

2. **Market Analysis**
   - Compare prices across different markets
   - Identify price disparities between regions

3. **Commodity Insights**
   - Analyze variety-wise price differences
   - Track grade-based price variations

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Contact

Your Name - [your.email@example.com]
Project Link: [https://github.com/yourusername/agri-price-analysis]

## Acknowledgments

- Ministry of Agriculture, Government of India
- National Informatics Centre
- Agricultural Market Information System
