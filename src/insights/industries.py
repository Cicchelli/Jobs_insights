from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        if not self.jobs_list:
            self.read(path="data/jobs.csv")  
        
        unique_industries = set(job["industry"] for job in self.jobs_list if job.get("industry"))
        return list(unique_industries)
