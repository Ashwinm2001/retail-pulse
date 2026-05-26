CREATE OR REPLACE TABLE `retail-pulse-496303.raw_data.dim_product` AS
SELECT DISTINCT
    Product_ID AS product_id,

    ROW_NUMBER() OVER(ORDER BY Product_ID) AS product_key,

    Category AS category,

    Sub_Category AS sub_category,

    Product_Name AS product_name

FROM `retail-pulse-496303.raw_data.superstore`;