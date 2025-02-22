from os import path
from typing import Union, Dict, List
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
        if not self.jobs_list:
            self.read(path)

        valid_min_salaries = [
            int(job["min_salary"])
            for job in self.jobs_list
            if job.get("min_salary") and job["min_salary"].isdigit()
        ]

        if not valid_min_salaries:
            raise ValueError("Nenhum salário mínimo válido encontrado.")

        min_salary = min(valid_min_salaries)
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        try:
            min_salary = float(job.get("min_salary", float("inf")))
            max_salary = float(job.get("max_salary", float("-inf")))

            if min_salary > max_salary:
                raise ValueError(
                    "Min_salary deve ser menor ou igual a max_salary."
                )

            salary = float(salary)
            return min_salary <= salary <= max_salary

        except (ValueError, TypeError, KeyError) as exc:
            raise ValueError(
                "Deve ser um número e a chave não pode estar vazia."
            ) from exc

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:

        filtered_jobs = []
        for job in jobs:
            try:
                if self.matches_salary_range(job, salary):
                    filtered_jobs.append(job)
            except ValueError:
                continue

        return filtered_jobs
