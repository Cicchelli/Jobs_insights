from typing import List, Dict
import csv


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, encoding="utf-8") as file:
            jobs = csv.DictReader(file)
            self.jobs_list.extend(jobs)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        job_types = set(job["job_type"] for job in self.jobs_list)
        return list(job_types)

    def filter_by_multiple_criteria(
        self, jobs: List[Dict], filters: Dict
    ) -> List[Dict]:
        if not isinstance(filters, dict):
            raise TypeError(
                "Os filtros devem ser fornecidos como um dicionário."
            )

        filtered_jobs = []
        for job in jobs:
            if all(job.get(key) == value for key, value in filters.items()):
                filtered_jobs.append(job)

        return filtered_jobs
