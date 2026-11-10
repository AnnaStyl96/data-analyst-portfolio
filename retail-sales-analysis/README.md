# Retail Sales Analysis | MySQL

A small SQL portfolio project built in MySQL Workbench. It uses three fictional customers and four sample purchases to compare customer spending, product revenue, and sales by customer country.

The [SQL script](retail_sales_analysis.sql) creates two related tables. `Customers` stores one row per customer, and `Sales` stores one row per purchase. The tables connect through `CustomerID`. Purchase amounts are in euros.

## Findings

| Question | Result |
| --- | --- |
| Which country generated the most revenue? | Greece generated €775 from 2 purchases. Germany generated €230 from 2 purchases. |
| Which product generated the most revenue? | Laptop led with €750, followed by Monitor (€200) and Mouse (€55). |
| How much did each customer spend? | Maria spent €775, Anna spent €230, and Nikos had no purchases (€0). |

Greece and Germany had the same number of purchases. Greece led on revenue because its purchases were worth more on average (€387.50 versus €115.00).

The analysis uses `INNER JOIN` for matching purchases to customers and `LEFT JOIN` for keeping customers without purchases. It also uses `SUM`, `COUNT`, `GROUP BY`, and `COALESCE`.

## Run in MySQL Workbench

Open `retail_sales_analysis.sql` in a local MySQL connection. On a fresh setup, run the full script once. If the sample tables and rows already exist, run `USE retail_sales_portfolio;` and then run only the queries under **Analysis**.
