# Sales Performance & Business Intelligence Dashboard

## Project Overview

This project is an end-to-end business intelligence and data analytics portfolio project focused on analysing the sales performance of a fictional Nigerian retail company over a 12-month period (January–December 2025).

The project demonstrates how Python, SQL and SQLite can be used to generate, manage, validate and analyse business data to uncover actionable insights that support decision-making.

**Project status:** Data engineering and SQL analysis completed. Power BI dashboard development in progress.

## Project Objectives

- Analyse sales performance across different months.
- Identify top-performing products and categories.
- Evaluate revenue contribution by customer segment.
- Compare sales performance across Nigerian regions.
- Examine monthly revenue growth.
- Assess the impact of discounts on sales.
- Develop business insights through SQL analysis and visualisation.

## Technology Stack

| Technology | Application |
|---|---|
| Python | Synthetic data generation and database loading |
| SQLite | Relational database management |
| SQL | Data validation, querying and business analysis |
| Microsoft Power BI | Interactive dashboard development (in progress) |
| Power Query | Data transformation (planned) |
| DAX | Business intelligence measures (planned) |
| Git & GitHub | Version control and project publication |

## Dataset Overview

The project uses synthetically generated Nigerian retail sales data.

| Dataset | Records |
|---|---:|
| Regions | 6 |
| Customers | 100 |
| Products | 25 |
| Sales transactions | 1,200 |
| Unique orders | 455 |

The sales dataset contains transaction dates, customer and product references, quantities, unit prices, discounts and calculated sales amounts.

## Key Business Findings

- **Total Revenue:** ₦615,491,675
- **Total Orders:** 455
- **Total Transactions:** 1,200
- **Units Sold:** 5,387
- **Average Order Value:** ₦1,352,728.96

### Revenue Performance

- August recorded the highest monthly revenue at ₦80,801,875.
- June followed with ₦78,668,375.
- May recorded the highest month-over-month revenue growth at 84.61%.

### Product Performance

- Laptop was the highest revenue-generating product at ₦106,502,500.
- Projector ranked second at ₦103,117,500.
- Electronics was the leading product category.

### Customer Segmentation

- Consumer customers generated ₦275,106,500.
- Small Business customers generated ₦184,842,500.
- Corporate customers generated ₦155,542,675.

### Regional Performance

- North East generated the highest regional revenue at ₦127,754,550.
- North West recorded the highest average order value at ₦1,611,482.89.

## Data Quality and Validation

The dataset was validated using SQL checks.

The validation confirmed:

- No missing required sales values.
- No duplicate transaction IDs.
- No invalid customer references.
- No invalid product references.
- No incorrect sales calculations.
- Every order belongs to one customer.
- Every order has one order date.

## Project Structure
