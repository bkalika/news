import psycopg2

DATABASE = {"database": "news", "user": "bohdan", "password": "bohdan", "port": 5432}
conn = psycopg2.connect(**DATABASE)
cur = None


def delete_votes(con) -> None:
    with con.cursor() as cursor:
        cursor.execute(
            """
            UPDATE news_api_post SET vote = 0
        """
        )
        con.commit()


delete_votes(conn)
