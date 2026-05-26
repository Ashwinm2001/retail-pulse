CREATE OR REPLACE TABLE retail_pulse.fact_sales AS
SELECT
  s.Order_ID,
  CAST(FORMAT_DATE('%Y%m%d', PARSE_DATE('%m/%d/%Y', s.Order_Date)) AS INT64) AS date_key,
  p.product_key,
  c.customer_key,
  st.store_key,
  s.Sales AS revenue,
  s.Profit AS profit,
  s.Quantity AS units_sold,
  s.Discount AS discount_pct,
  ROUND(s.Profit / NULLIF(s.Sales, 0) * 100, 2) AS profit_margin_pct
FROM raw_data.superstore s
LEFT JOIN retail_pulse.dim_product p USING (Product_ID)
LEFT JOIN retail_pulse.dim_customer c USING (Customer_ID)
LEFT JOIN retail_pulse.dim_store st USING (State)
LEFT JOIN retail_pulse.dim_date d ON d.full_date = PARSE_DATE('%m/%d/%Y', s.Order_Date);