import sqlite3
import pandas as pd
import requests
import os

# 1. Auto-Download the Chinook Database (if not present)
db_file = 'chinook.db'
url = "https://github.com/lerocha/chinook-database/raw/master/ChinookDatabase/DataSources/Chinook_Sqlite.sqlite"

if not os.path.exists(db_file):
    print("Downloading Chinook Database...")
    r = requests.get(url)
    with open(db_file, 'wb') as f:
        f.write(r.content)
    print("Download Complete!")
else:
    print("Database already exists.")

# 2. Connect to the Database
conn = sqlite3.connect(db_file)

# ============================================================
# ANALYSIS 1: Which City generates the most revenue?
# Skills: JOIN, GROUP BY, ORDER BY, AGGREGATION
# ============================================================
query_city = """
SELECT 
    BillingCity, 
    ROUND(SUM(Total), 2) as Total_Revenue
FROM Invoice
GROUP BY BillingCity
ORDER BY Total_Revenue DESC
LIMIT 10;
"""
print("\n--- TOP 10 REVENUE CITIES ---")
df_city = pd.read_sql(query_city, conn)
print(df_city)
df_city.to_csv('sql_revenue_by_city.csv', index=False)


# ============================================================
# ANALYSIS 2: Who are the Best-Selling Artists?
# Skills: COMPLEX JOINS (3 tables), AGGREGATION
# Logic: InvoiceLine -> Track -> Album -> Artist
# ============================================================
query_artist = """
SELECT 
    ar.Name as Artist_Name,
    COUNT(il.InvoiceLineId) as Total_Sales
FROM InvoiceLine il
JOIN Track t ON il.TrackId = t.TrackId
JOIN Album al ON t.AlbumId = al.AlbumId
JOIN Artist ar ON al.ArtistId = ar.ArtistId
GROUP BY ar.Name
ORDER BY Total_Sales DESC
LIMIT 5;
"""
print("\n--- TOP 5 SELLING ARTISTS ---")
df_artist = pd.read_sql(query_artist, conn)
print(df_artist)
df_artist.to_csv('sql_top_artists.csv', index=False)


# ============================================================
# ANALYSIS 3: Customer Lifetime Value (CLV)
# Skills: JOINS, ROUND, ALIASING
# ============================================================
query_customer = """
SELECT 
    c.FirstName || ' ' || c.LastName as Customer_Name,
    c.Country,
    COUNT(i.InvoiceId) as Purchase_Count,
    ROUND(SUM(i.Total), 2) as Total_Spent
FROM Customer c
JOIN Invoice i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId
ORDER BY Total_Spent DESC
LIMIT 5;
"""
print("\n--- TOP 5 VIP CUSTOMERS ---")
df_customer = pd.read_sql(query_customer, conn)
print(df_customer)
df_customer.to_csv('sql_vip_customers.csv', index=False)

print("-" * 30)
print("SUCCESS! SQL Analysis complete. CSV files saved.")
conn.close()
