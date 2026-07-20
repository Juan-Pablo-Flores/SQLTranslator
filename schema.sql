-- Simple e-commerce schema

CREATE TABLE users (id SERIAL PRIMARY KEY, first_name VARHCAR(50), last_name VARCHAR(50), email VARCHAR(255) UNIQUE);
CREATE TABLE categories (id SERIAL PRIMARY KEY, name VARCHAR(100) UNIQUE);
CREATE TABLE products (id SERIAL PRIMARY KEY, category_id INT REFERENCES categories(id), name VARCHAR(255), price DECIMAL(10,2), stock_quantity INT);
CREATE TABLE orders (id SERIAL PRIMARY KEY, user_id INT REFERENCES users(id), order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
CREATE TABLE order_items (order_id INT REFERENCES orders(id), product_id INT REFERENCES products(id), quantity INT, price_at_purchase DECIMAL(10,2));