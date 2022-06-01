from src.commom import create_connection
import pandas as pd
from tabulate import tabulate


query1 = """
SELECT (SELECT count(*) total FROM person_data) AS                 total_users,
       count(*)                                                    from_germany_using_gmail,
       count(*) * 100.0 / (SELECT count(*) total FROM person_data) percentage
FROM person_data
WHERE address_country = 'Germany'
  AND email = 'gmail'
"""

query2 = """
SELECT address_country, count(*) AS user_count
FROM person_data
WHERE email = 'gmail'
GROUP BY address_country
ORDER BY user_count DESC
LIMIT 3
"""

query3 = """
SELECT count(*) user_count
FROM person_data
WHERE birthday > '60'
  AND email = 'gmail'
LIMIT 100
"""


def _tabulate_data(data):
    print(tabulate(data, headers="keys", tablefmt="psql"))


def main():
    try:
        print("Generating report")

        TABLE_NAME = "person_data"
        conn = create_connection(TABLE_NAME)
        df1 = pd.read_sql(query1, conn)
        df2 = pd.read_sql(query2, conn)
        df3 = pd.read_sql(query3, conn)

        print("-" * 100)
        print(
            "Which percentage of users live in Germany and use Gmail as an email provider?"
        )
        _tabulate_data(df1)
        print("-" * 100)

        print(
            "Which are the top three countries in our database that use Gmail as an email provider?"
        )
        _tabulate_data(df2)
        print("-" * 100)

        print("How many people over 60 years use Gmail as an email provider?")
        _tabulate_data(df3)
    except Exception as err:
        print("Failed to generate report", {"error": err})
