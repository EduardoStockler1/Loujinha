# Loujinha  
Stock Management System with Order Automation:  
- A system that monitors a store or warehouse inventory, alerts for low-stock items, and even automates reordering. It includes features like sales reports, demand forecasting, and trend analysis.

## Built With  
- **Django**: A high-level Python web framework for rapid development and clean design.  
- **Python**: Used for scripting and backend logic.  
- **SQLite**: For lightweight and efficient database management.

## Getting Started  
Follow these instructions to set up and run the project locally.

### Prerequisites  
- **Python 3.9 or higher**  
- **Pip** (Python package manager)  
- **Django** (installable via pip)

### Installation  
1. Clone the repository:  
   ```bash
   git clone https://github.com/EduardoStockler1/Loujinha.git
   cd Loujinha
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations to set up the database:  
   ```bash
   python manage.py migrate
   ```

4. Create a superuser for admin access (optional):  
   ```bash
   python manage.py createsuperuser
   ```

### Running the Application  
Start the development server:  
```bash
python manage.py runserver
```

Access the application in your browser at `http://127.0.0.1:8000`.

## Features  
- **Product Catalog**: Add, view, and manage product details.  
- **Inventory Management**: Monitor stock levels and get alerts for low stock.  
- **Order Automation**: Automatically create reorders based on stock levels.  
- **Reporting**: Generate sales and trend analysis reports.

## License  
This project is licensed under the MIT License. See the LICENSE file for more details.

---

By Eduardo Stockler.
```  
 