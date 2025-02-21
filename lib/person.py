#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John Doe", job="Admin"):
        # Use the property setters for validation.
        self.name = name
        self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # Ensure name is a string between 1 and 25 characters,
        # and convert it to title case before saving.
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        # Ensure the job is one of the approved jobs.
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
