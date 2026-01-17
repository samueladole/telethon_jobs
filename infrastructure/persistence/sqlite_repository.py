import sqlite3
from app.domain.entities.job_posting import JobPosting
from app.interfaces.repositories import JobRepository


class SQLiteJobRepository(JobRepository):
    """SQLite implementation of the JobRepository protocol."""
    def __init__(self, db_path: str = "jobs.db"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute(
            """CREATE TABLE IF NOT EXISTS jobs (
                id TEXT PRIMARY KEY,
                title TEXT,
                description TEXT,
                url TEXT
            )"""
        )

    def save(self, job: JobPosting) -> None:
        """Saves a job posting to the SQLite database."""
        self.conn.execute(
            "INSERT OR IGNORE INTO jobs VALUES (?, ?, ?, ?)",
            (job.id, job.title, job.description, job.source_url),
        )
        self.conn.commit()
