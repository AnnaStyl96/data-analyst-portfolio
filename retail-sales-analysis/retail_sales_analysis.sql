-- Retail Sales Analysis | MySQL
-- Run the setup once in a fresh schema. If the sample tables already
-- exist and contain the sample data, run USE and the analysis only.

CREATE DATABASE IF NOT EXISTS retail_sales_portfolio;
USE retail_sales_portfolio;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100) NOT NULL,
    Country VARCHAR(50) NOT NULL
);

CREATE TABLE Sales (
    SaleID INT PRIMARY KEY,
    CustomerID INT NOT NULL,
    Product VARCHAR(100) NOT NULL,
    Amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Customers (CustomerID, CustomerName, Country)
VALUES
    (101, 'Maria', 'Greece'),
    (102, 'Nikos', 'Greece'),
    (103, 'Anna', 'Germany');

INSERT INTO Sales (SaleID, CustomerID, Product, Amount)
VALUES
    (1, 101, 'Laptop', 750.00),
    (2, 101, 'Mouse', 25.00),
    (3, 103, 'Monitor', 200.00),
    (4, 103, 'Mouse', 30.00);

-- Analysis

-- 1. Which customer made each purchase?
SELECT c.CustomerName, s.Product, s.Amount
FROM Customers AS c
INNER JOIN Sales AS s
    ON c.CustomerID = s.CustomerID
ORDER BY s.SaleID;

-- 2. Which customers have never made a purchase?
SELECT c.CustomerID, c.CustomerName
FROM Customers AS c
LEFT JOIN Sales AS s
    ON c.CustomerID = s.CustomerID
WHERE s.CustomerID IS NULL
ORDER BY c.CustomerID;

-- 3. How much did each customer spend, including customers without purchases?
SELECT c.CustomerName, COALESCE(SUM(s.Amount), 0) AS TotalSpent
FROM Customers AS c
LEFT JOIN Sales AS s
    ON c.CustomerID = s.CustomerID
GROUP BY c.CustomerID, c.CustomerName
ORDER BY TotalSpent DESC, c.CustomerID;

-- 4. Which products generated the most revenue?
SELECT Product, SUM(Amount) AS TotalSales
FROM Sales
GROUP BY Product
ORDER BY TotalSales DESC, Product;

-- 5. How do revenue and purchase count compare by customer country?
SELECT c.Country, SUM(s.Amount) AS TotalSales, COUNT(s.SaleID) AS SalesCount
FROM Customers AS c
INNER JOIN Sales AS s
    ON c.CustomerID = s.CustomerID
GROUP BY c.Country
ORDER BY TotalSales DESC;
