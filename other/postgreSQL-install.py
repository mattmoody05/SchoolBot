PASSWORD = ""


import asyncpg
import asyncio

async def main():
    conn = await asyncpg.connect(host = "localhost", user = "postgres", database = "postgres", port = "5432", password = PASSWORD)
    query = """CREATE TABLE study_mode(
        user_id BIGINT NOT NULL,
        mode BOOL NOT NULL
    )"""
    await conn.execute(query)

if __name__ == '__main__':
    task = asyncio.get_event_loop()
    task.run_until_complete(main())
