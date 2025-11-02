SELECT product, SUM(amount) AS total_sales
FROM sales_data
GROUP BY product
ORDER BY total_sales DESC;
