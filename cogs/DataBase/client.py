import asyncpg


class DataBase:
    def __init__(self, client, pool):
        self.client = client
        self.pool = pool

    @classmethod
    async def create_pool(cls, client, info):
        pool = await asyncpg.create_pool(**info)
        self = cls(client=client, pool=pool)
        print(f"Established connection with the DataBase to - {info}")
        return self

    async def check_study_mode(self, user_id: int):
        query = """SELECT mode FROM study_mode WHERE user_id=$1"""
        record = await self.pool.fetch(query, user_id)
        return record

    async def insert_study_mode(self, user_id: int):
        query = """INSERT INTO study_mode (user_id, mode) VALUES ($1, $2)"""
        await self.pool.execute(query, user_id, True)

    async def change_study_mode(self, user_id: int, mode: bool):
        query = """UPDATE study_mode SET mode=$2 WHERE user_id=$1"""
        await self.pool.execute(query, user_id, mode)

    async def fetch_all_study_modes(self):
        query = """SELECT user_id FROM study_mode WHERE mode=$1"""
        record = await self.pool.fetch(query, True)
        return record

    async def insert_time_table(self, day: str, user_id: int, time: str, work: str):
        query = """INSERT INTO time_table (day, user_id, time, work) VALUES ($1, $2, $3, $4)"""
        await self.pool.execute(query, day, user_id, time, work)

    async def check_todays_time_table(self, day, time):
        query = """SELECT user_id, work FROM time_table WHERE day=$1 AND time=$2"""
        record = await self.pool.fetch(query, day, time)
        return record

    async def check_if_in_time_table(self, day: str, user_id: int, time: str):
        query = """SELECT * FROM time_table WHERE day=$1 AND user_id=$2 AND time=$3"""
        record = await self.pool.fetch(query, day, user_id, time)
        return record

    async def delete_from_time_table(self, day: str, user_id: int, time: str):
        query = """DELETE FROM time_table WHERE day=$1 AND user_id=$2 AND time=$3"""
        await self.pool.execute(query, day, user_id, time)

    async def select_all_from_time_table(self, user_id: int):
        query = """SELECT day, time, work FROM time_table WHERE user_id=$1"""
        record = await self.pool.fetch(query, user_id)
        return record

    async def insert_into_todo(self, user_id: int, work: str, time: str):
        query = """INSERT INTO todo (user_id, work, time) VALUES ($1, $2, $3)"""
        await self.pool.execute(query, user_id, work, time)

    async def check_from_todo(self, user_id: int, work: str):
        query = """SELECT * FROM todo WHERE user_id=$1 AND work=$2"""
        record = await self.pool.fetch(query, user_id, work)
        return record

    async def delete_from_todo(self, user_id: int, work: str):
        query = """DELETE FROM todo WHERE user_id=$1 AND work=$2"""
        await self.pool.execute(query, user_id, work)

    async def select_all_from_todo(self, user_id: int):
        query = """SELECT * FROM todo WHERE user_id=$1"""
        record = await self.pool.fetch(query, user_id)
        return record

    async def insert_into_tag(self, user_id: int, name: str, text: str):
        query = """INSERT INTO tag (user_id, name, text, uses) VALUES ($1, $2, $3, $4)"""
        await self.pool.execute(query, user_id, name, text, 0)

    async def update_uses_in_tag(self, name: str):
        record = await self.select_from_tag(name)
        numbers = int(record[0]["uses"])
        numbers += 1
        query = """UPDATE tag SET uses=$2 WHERE name=$1"""
        await self.pool.execute(query, name, numbers)

    async def select_from_tag(self, name: str):
        query = """SELECT * FROM tag WHERE name=$1"""
        record = await self.pool.fetch(query, name)
        return record

    async def select_user_tag(self, user_id: int, name: str):
        query = """SELECT * FROM tag WHERE user_id=$1 AND name=$2"""
        record = await self.pool.fetch(query, user_id, name)
        return record

    async def delete_from_tag(self, user_id: int, name: str):
        query = """DELETE FROM tag WHERE user_id=$1 AND name=$2"""
        await self.pool.execute(query, user_id, name)

    async def rename_from_tag(self, user_id: int, name: str, new_name: str):
        query = """UPDATE tag SET name=$3 WHERE user_id=$1 AND name=$2"""
        await self.pool.execute(query, user_id, name, new_name)

    async def edit_from_tag(self, user_id: int, name: str, content: str):
        query = """UPDATE tag SET text=$3 WHERE user_id=$1 AND name=$2"""
        await self.pool.execute(query, user_id, name, content)

    async def select_all_from_tag(self):
        query = """SELECT name FROM tag ORDER BY name"""
        record = await self.pool.fetch(query)
        return record

    async def select_tag_of_member(self, user_id: int):
        query = """SELECT name FROM tag WHERE user_id=$1 ORDER BY name"""
        record = await self.pool.fetch(query, user_id)
        return record

    async def info_of_tag(self, name: str):
        query = """SELECT * FROM tag WHERE name=$1"""
        record = await self.pool.fetch(query, name)
        return record
