
-- 1. Monthly sales performance
SELECT
    strftime('%Y-%m', order_date) AS sales_month,
    COUNT(*) AS transactions,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(sales_amount), 2) AS revenue
FROM sales
GROUP BY sales_month
ORDER BY sales_month;


-- 2. Overall business KPIs
SELECT
    ROUND(SUM(sales_amount), 2) AS total_revenue,
    COUNT(DISTINCT order_id) AS total_orders,
    COUNT(*) AS total_transactions,
    SUM(quantity) AS units_sold,
    ROUND(
        SUM(sales_amount) / COUNT(DISTINCT order_id), 2
    ) AS average_order_value
FROM sales;


-- 3. Top 10 products by revenue
SELECT
    p.product_name,
    p.category,
    SUM(s.quantity) AS units_sold,
    COUNT(*) AS transactions,
    ROUND(SUM(s.sales_amount), 2) AS revenue
FROM sales s
JOIN products p
    ON s.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY revenue DESC
LIMIT 10;


-- 4. Revenue by customer segment
SELECT
    c.customer_segment,
    COUNT(DISTINCT s.order_id) AS total_orders,
    COUNT(DISTINCT c.customer_id) AS customers,
    ROUND(SUM(s.sales_amount), 2) AS revenue,
    ROUND(
        SUM(s.sales_amount) /
        COUNT(DISTINCT s.order_id), 2
    ) AS average_order_value
FROM sales s
JOIN customers c
    ON s.customer_id = c.customer_id
GROUP BY c.customer_segment
ORDER BY revenue DESC;


-- 5. Regional sales performance
SELECT
    r.region_name,
    COUNT(DISTINCT c.customer_id) AS customers,
    COUNT(DISTINCT s.order_id) AS total_orders,
    SUM(s.quantity) AS units_sold,
    ROUND(SUM(s.sales_amount), 2) AS revenue,
    ROUND(
        SUM(s.sales_amount) /
        COUNT(DISTINCT s.order_id), 2
    ) AS average_order_value
FROM sales s
JOIN customers c
    ON s.customer_id = c.customer_id
JOIN regions r
    ON c.region_id = r.region_id
GROUP BY r.region_id, r.region_name
ORDER BY revenue DESC;


-- 6. Monthly revenue growth
WITH monthly_sales AS (
    SELECT
        strftime('%Y-%m', order_date) AS sales_month,
        SUM(sales_amount) AS revenue
    FROM sales
    GROUP BY sales_month
)
SELECT
    sales_month,
    ROUND(revenue, 2) AS revenue,
    ROUND(
        LAG(revenue) OVER (ORDER BY sales_month), 2
    ) AS previous_month_revenue,
    ROUND(
        (revenue - LAG(revenue) OVER (ORDER BY sales_month))
        * 100.0 /
        NULLIF(LAG(revenue) OVER (ORDER BY sales_month), 0),
        2
    ) AS growth_percentage
FROM monthly_sales
ORDER BY sales_month;


-- 7. Discount performance
SELECT
    CASE
        WHEN discount_pct = 0 THEN 'No Discount'
        WHEN discount_pct <= 0.05 THEN 'Up to 5%'
        WHEN discount_pct <= 0.10 THEN '6% to 10%'
        ELSE 'Above 10%'
    END AS discount_band,
    COUNT(*) AS transactions,
    SUM(quantity) AS units_sold,
    ROUND(SUM(sales_amount), 2) AS revenue
FROM sales
GROUP BY discount_band
ORDER BY revenue DESC;
