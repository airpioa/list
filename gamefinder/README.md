# Game Finder

This project is a web scraper that pulls game websites from Google search results. It is designed to demonstrate how to perform web scraping using Python.

## Project Structure

```
my-python-app
├── src
│   ├── main.py          # Entry point of the application
│   └── utils
│       └── scraper.py   # Contains the Scraper class for fetching and parsing results
├── requirements.txt     # Lists the dependencies required for the project
└── README.md            # Documentation for the project
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/my-python-app.git
   ```

2. Navigate to the project directory:
   ```
   cd my-python-app
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

This will initialize the scraper and pull game websites from Google.

## Dependencies

This project requires the following Python packages:
- requests
- beautifulsoup4

Make sure to install these packages using the `requirements.txt` file provided.