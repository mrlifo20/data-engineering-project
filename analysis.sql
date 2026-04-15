-- Top 5 Customers
SELECT TOP 5 Customer_Name, SUM(Sales) AS Total_Spent
FROM sales1
GROUP BY Customer_Name
ORDER BY Total_Spent DESC;

-- Sales by Category
SELECT Category, SUM(Sales) AS Total_Sales
FROM sales1
GROUP BY Category
ORDER BY Total_Sales DESC;

-- Profit by Region
SELECT Region, SUM(Profit) AS Total_Profit
FROM sales1
GROUP BY Region
ORDER BY Total_Profit DESC;

-- Monthly Sales
SELECT Order_Year, Order_Month, SUM(Sales) AS Monthly_Sales
FROM sales1
GROUP BY Order_Year, Order_Month
ORDER BY Order_Year, Order_Month;