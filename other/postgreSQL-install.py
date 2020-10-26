PASSWORD = ""
PORT = 5432

import asyncpg
import asyncio

async def main():
    conn = await asyncpg.connect(host = "localhost", user = "postgres", database = "postgres", port = PORT, password = PASSWORD)

    # study_mode
    study_mode_query = """CREATE TABLE study_mode(
        user_id BIGINT NOT NULL,
        mode BOOL NOT NULL
    )"""
    await conn.execute(study_mode_query)

    # tag
    tag_query = """CREATE TABLE tag(
        user_id BIGINT NOT NULL,
        name TEXT NOT NULL,
        text TEXT NOT NULL,
        uses INT NOT NULL
    )"""
    await conn.execute(tag_query)

    # todo
    todo_query = """CREATE TABLE todo(
        user_id BIGINT NOT NULL,
        work TEXT NOT NULL,
        time TEXT NOT NULL
    )"""
    await conn.execute(todo_query)

    # time_table
    time_table_query = """CREATE TABLE time_table(
        day TEXT NOT NULL,
        user_id BIGINT NOT NULL,
        time TEXT NOT NULL,
        work TEXT NOT NULL
    )"""
    await conn.execute(time_table_query)

if __name__ == '__main__':
    task = asyncio.get_event_loop()
    task.run_until_complete(main())
