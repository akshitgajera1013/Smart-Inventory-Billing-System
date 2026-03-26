🏪 Smart Inventory & Billing System

A full-stack Inventory Management & Billing System built using Python, Streamlit, and PostgreSQL.
This application helps businesses efficiently manage customers, products, sales, billing, and analytics in a modern dashboard interface.

🚀 Features
📊 Dashboard

Overview of total customers, products, and sales

Real-time metrics display

👥 Customer Management

Add, view, update, and delete customers

Store customer name and contact details

📦 Product Management

Add, update, delete, and view products

Track product price and stock quantity

💰 Sales Management

Create new sales transactions

Add multiple products to a sale

Automatic total calculation

Generate detailed bills

🧾 Billing System

Generate invoice with:

Customer details

Product list

Quantity & price

Total amount

📈 Analytics & Reports

Sales summary (total revenue & count)

Sales by date range

Top selling products

Low stock alerts

Customer purchase history

🛠️ Tech Stack

Frontend: Streamlit

Backend: Python

Database: PostgreSQL

Database Connector: psycopg2

📂 Project Structure

Smart-Inventory-System/

        ├── app.py                  
        ├── database.py           
        ├── customers.py            
        ├── products.py             
        ├── sales.py                
        ├── sales_item.py          
        ├── requirements.txt
        └── README.md               

📊 Database Design
Tables:

customers

products

sales

sale_items

Relationships:

One customer → many sales

One sale → many sale items

One product → many sale items

