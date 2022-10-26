"""Module for the RowData model."""

from dataclasses import dataclass


@dataclass
class RowData:
    """Class representing a row/entry in the dataset in the database.
    Instance Attributes:
      - self.entity: the country/location/category the data entry belongs to
      - self.year: the year of the row data
      - self.undernourishment: the prevalence of undernourishment as a percentage of the population
    """
    name: str
    year: int
    undernourishment: float
