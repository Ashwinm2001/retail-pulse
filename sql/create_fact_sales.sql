CREATE OR REPLACE TABLE `retail-pulse-496303.raw_data.fact_sales` AS
SELECT
    GENERATE_UUID() AS order_id,

    TIMESTAMP(Order_Date) AS order_date,

    Customer_Name AS customer_name,

    Product_ID AS product_id,

    CAST(Sales AS INT64) AS sales,

    CAST(Profit AS FLOAT64) AS profit,

    CAST(Quantity AS INT64) AS quantity

FROM `retail-pulse-496303.raw_data.superstore`;