# Split Bill

## Description
This is a Python-based console application that calculates and fairly splits bills between flatmates based on their stay duration. It also generates a PDF report summarizing the bill and individual contributions.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)
- [PDF Report Details](#pdf-report-details)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Input Validation**: Ensures valid inputs for bill amount, period, and flatmate details.
- **Fair Calculation**: Splits the bill based on the number of days each flatmate stayed in the house.
- **PDF Report**: Generates a PDF report summarizing the bill and payment details.
- **User-Friendly**: Simple command-line interface for ease of use.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Split_Bill.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Split_Bill
   ```
3. Ensure you have Python installed (version 3.x recommended).

## Usage
1. Run the program:
   ```bash
   python main.py
   ```
2. Follow the prompts to enter:
   - The bill amount.
   - The billing period (e.g., December 2023).
   - The type of expense (e.g., Rent, Utilities).
   - The names of the flatmates and the number of days they stayed in the house.
3. The application will:
   - Calculate each flatmate's share.
   - Generate a PDF report in the `resources/output` folder.
   - Automatically open the generated PDF report in your default browser.

## Project Structure
```
Split_Bill/
├── main.py                # Main script to run the application
├── bill.py                # Bill class to store bill details
├── flatmate.py            # Flatmate class to store flatmate details
├── utils.py               # Utility functions for input validation
├── pdf_report.py          # PDF report generation
├── resources/
│   ├── house.png          # Image used in the PDF report
│   └── output/            # Folder to store generated PDF reports
└── README.md              # Project documentation
```

## Dependencies
- **Python 3.x**
- **Libraries**:
  - `fpdf` (for generating PDF reports)
  - `webbrowser` (for opening the generated PDF)

To install the required libraries, run:
```bash
pip install fpdf
```

## PDF Report Details
The PDF report includes:
- A title (*Split Bill*).
- An icon (*house.png*) from the resources folder.
- The billing period and expense type.
- The names of the flatmates and their respective payment amounts.
- The report is saved in the `resources/output` folder with the filename format: `<Period>_<ExpenseType>.pdf`.

## Contributing
Contributions are welcome! If you'd like to contribute:
1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Submit a pull request with a detailed description of your changes.

## License
This project is licensed under the MIT License.

## Author
- **Shubham Vaishnav**
