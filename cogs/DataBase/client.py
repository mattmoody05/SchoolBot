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