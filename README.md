# inventory_management_system

## Project Overview

The **Inventory Management System** is a Python-based application designed to help businesses manage their inventory efficiently. The system allows users to track products, transactions, and suppliers, providing a comprehensive solution for inventory management.

## Features

- **Product Management**: Add, update, delete, and list products.
- **Transaction Management**: Record and manage transactions related to product sales.
- **Supplier Management**: Add, update, delete, and list suppliers.
- **Comprehensive Reports**: Generate reports on inventory status and transaction history.

## Installation

### Prerequisites

Ensure you have the following installed on your machine:

- Python 3.x
- SQLite3

### Steps

1. **Clone the repository**:
    ```sh
    git clone https://github.com/NguyoVictor/inventory_management_system
    ```
2. **Navigate to the project directory**:
    ```sh
    cd inventory_management_system
    ```
3. **Initialize the database**:
    ```sh
    python app.py
    ```

## Usage

1. **Run the application**:
    ```sh
    python lib/clip.py menu
    ```
2. **Follow the on-screen instructions** to manage products, transactions, and suppliers.

## Project Structure

```
inventory-management-system/
├── database/
│   ├── connection.py
│   └── setup.py
├── models/
│   ├── product.py
│   ├── transaction.py
│   ├── supplier.py
├── app.py
├── helpers.py
├── README.md
└── requirements.txt
```

### Database Folder

- **connection.py**: Manages the database connection.
- **setup.py**: Initializes the database and creates necessary tables.

### Models Folder

- **product.py**: Defines the Product class for product management.
- **transaction.py**: Defines the Transaction class for managing transactions.
- **supplier.py**: Defines the Supplier class for supplier management.

### Main Application

- **app.py**: The main application file that runs the program and provides a CLI for user interaction.
- **helpers.py**: Contains helper functions for performing various operations like listing, adding, updating, and deleting records.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## Author

Victor Nguyo

## License

This project is licensed under the MIT License

## Acknowledgements

- Thanks to all contributors and open-source projects that made this project possible.

---

Feel free to customize this README file according to your specific project details and requirements.