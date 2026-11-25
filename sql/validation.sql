
-- 1. Count all records
SELECT 'Sales Records' AS metric, COUNT(*) AS result
FROM sales

UNION ALL

SELECT 'Unique Orders', COUNT(DISTINCT order_id)
FROM sales

UNION ALL

SELECT 'Customers', COUNT(*)
FROM customers

UNION ALL

SELECT 'Products', COUNT(*)
FROM products

UNION ALL

SELECT 'Regions', COUNT(*)
FROM regions;


-- 2. Calculate total sales revenue
SELECT
    ROUND(SUM(sales_amount), 2) AS total_revenue
FROM sales;


-- 3. Find duplicate transaction IDs
SELECT
    transaction_id,
    COUNT(*) AS occurrences
FROM sales
GROUP BY transaction_id
HAVING COUNT(*) > 1;


-- 4. Check missing required values
SELECT COUNT(*) AS missing_values
FROM sales
WHERE transaction_id IS NULL
   OR order_id IS NULL
   OR order_date IS NULL
   OR customer_id IS NULL
   OR product_id IS NULL
   OR quantity IS NULL
   OR unit_price IS NULL
   OR discount_pct IS NULL
   OR sales_amount IS NULL;


-- 5. Find sales with invalid customer references
SELECT COUNT(*) AS invalid_customer_references
FROM sales s
LEFT JOIN customers c
    ON s.customer_id = c.customer_id
WHERE c.customer_id IS NULL;


-- 6. Find sales with invalid product references
SELECT COUNT(*) AS invalid_product_references
FROM sales s
LEFT JOIN products p
    ON s.product_id = p.product_id
WHERE p.product_id IS NULL;


-- 7. Verify sales calculations
SELECT COUNT(*) AS incorrect_sales_calculations
FROM sales
WHERE ABS(
    sales_amount -
    (quantity * unit_price * (1 - discount_pct))
) > 0.01;


-- 8. Sales by product category
SELECT
    p.category,
    COUNT(*) AS transaction_count,
    SUM(s.quantity) AS units_sold,
    ROUND(SUM(s.sales_amount), 2) AS revenue
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;


-- 9. Sales by region
SELECT
    r.region_name,
    COUNT(DISTINCT s.order_id) AS total_orders,
    ROUND(SUM(s.sales_amount), 2) AS revenue
FROM sales s
JOIN customers c
    ON s.customer_id = c.customer_id
JOIN regions r
    ON c.region_id = r.region_id
GROUP BY r.region_name
ORDER BY revenue DESC;


-- 10. Check whether an order has multiple customers
SELECT
    order_id,
    COUNT(DISTINCT customer_id) AS customer_count
FROM sales
GROUP BY order_id
HAVING COUNT(DISTINCT customer_id) > 1;


-- 11. Check whether an order has multiple dates
SELECT
    order_id,
    COUNT(DISTINCT order_date) AS date_count
FROM sales
GROUP BY order_id
HAVING COUNT(DISTINCT order_date) > 1;


-- 12. Verify that every order belongs to one customer
SELECT
    COUNT(*) AS orders_with_multiple_customers
FROM (
    SELECT order_id
    FROM sales
    GROUP BY order_id
    HAVING COUNT(DISTINCT customer_id) > 1
);


-- 13. Verify that every order has one order date
SELECT
    COUNT(*) AS orders_with_multiple_dates
FROM (
    SELECT order_id
    FROM sales
    GROUP BY order_id
    HAVING COUNT(DISTINCT order_date) > 1
);
