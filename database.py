import sqlalchemy
from sqlalchemy import create_engine, text

engine = create_engine(
    'postgresql://rbabu:talktome@192.168.0.126:5432/safehouse')


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.all():
            jobs.append(dict(row))
        return jobs
