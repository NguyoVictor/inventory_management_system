import sys
import os
import click

# Ensure the lib directory is in the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.helpers import init_db, get_session
from lib.models.model_1 import Product, Transaction, Supplier

# Ensure the lib directory is in the PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@click.group()
def cli():
    pass

def show_menu():
    click.echo("Inventory Management System")
    click.echo("1. Initialize the database")
    click.echo("2. Add a new product")
    click.echo("3. Adjust stock")
    click.echo("4. View product details")
    click.echo("5. List all products")
    click.echo("6. Exit")

@cli.command()
def menu():
    """Show the main menu."""
    while True:
        show_menu()
        choice = click.prompt("Please choose an option", type=int)

        if choice == 1:
            initdb()
        elif choice == 2:
            add_product()
        elif choice == 3:
            adjust_stock()
        elif choice == 4:
            view_product()
        elif choice == 5:
            list_products()
        elif choice == 6:
            click.echo("Exiting...")
            break
        else:
            click.echo("Invalid choice, please try again.")

def initdb():
    """Initialize the database."""
    init_db()
    click.echo("Initialized the database.")

def add_product():
    """Add a new product."""
    name = click.prompt("Please enter the product name")
    category = click.prompt("Please enter the product category")
    session = get_session()
    product = Product(product_name=name, category=category)
    session.add(product)
    session.commit()
    click.echo(f"Added product {name} in category {category}.")

def adjust_stock():
    """Adjust the stock for a product."""
    product_id = click.prompt("Please enter the product ID", type=int)
    quantity = click.prompt("Please enter the quantity to adjust", type=int)
    session = get_session()
    transaction = Transaction(product_id=product_id, quantity=quantity)
    session.add(transaction)
    session.commit()
    click.echo(f"Adjusted stock for product ID {product_id} by {quantity} units.")

def view_product():
    """View details of a product."""
    product_id = click.prompt("Please enter the product ID", type=int)
    session = get_session()
    product = session.query(Product).filter_by(product_id=product_id).first()
    if product:
        transactions = session.query(Transaction).filter_by(product_id=product_id).all()
        click.echo(f"Product: {product.product_name}, Category: {product.category}")
        for t in transactions:
            click.echo(f"  Transaction: {t.transaction_id}, Quantity: {t.quantity}, Date: {t.date}")
    else:
        click.echo(f"No product found with ID {product_id}")

def list_products():
    """List all products."""
    session = get_session()
    products = session.query(Product).all()
    for product in products:
        click.echo(f"Product ID: {product.product_id}, Name: {product.product_name}, Category: {product.category}")

if __name__ == '__main__':
    cli.add_command(menu)
    cli()


    
