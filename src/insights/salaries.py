from os import path
from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self) -> int:
        if not self.jobs_list:
            self.read(path) 
            
        max_salary_list = [
            int(job["max_salary"])
            for job in self.jobs_list
            if job.get("max_salary") and job["max_salary"].isdigit()
        ]
        
        if not max_salary_list:
            raise ValueError("Nenhum salário máximo válido encontrado.")
        
        max_salary = max(max_salary_list)
        print(max_salary)
        return max_salary
    
    def get_min_salary(self) -> int:
        pass

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
