import collections
from datetime import date
import pandas as pd


class Transformer:
    def __init__(self):
        self.maintain_data = ["email", "birthday", "address_country"]

    def _flatten(self, d, parent_key="", sep="_"):
        items = []
        for k, v in d.items():
            new_key = parent_key + sep + k if parent_key else k
            if isinstance(v, collections.MutableMapping):
                items.extend(self._flatten(v, new_key, sep=sep).items())
            else:
                items.append((new_key, v))
        return dict(items)

    def anonymize_data(self, data: list) -> list:
        __anonymized_data = []
        for row in data:
            row = self._flatten(row)
            anonymized_data = {}
            for idx, value in row.items():
                if idx not in self.maintain_data:
                    anonymized_data[idx] = "****"
                else:
                    anonymized_data[idx] = value
            __anonymized_data.append(anonymized_data)
        return __anonymized_data

    def _get_user_age(self, birthday: str) -> str:
        year = birthday.split("-")[0]
        current_year = date.today().year
        age = int(current_year) - int(year)
        if age >= 0 and age <= 10:
            return "0-10"
        elif age > 10 and age <= 20:
            return "10-20"
        elif age > 20 and age <= 30:
            return "20-30"
        elif age > 30 and age <= 40:
            return "30-40"
        elif age > 40 and age <= 50:
            return "40-50"
        elif age > 50 and age <= 60:
            return "50-60"
        elif age > 60 and age <= 70:
            return "60-70"
        elif age > 70 and age <= 80:
            return "70-80"
        elif age > 80 and age <= 90:
            return "80-90"
        else:
            return "90+"

    def _get_email_provider(self, email: str) -> str:
        provider = email.split("@")[1].split(".")[0]
        return provider

    def data_generalization(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        dataframe["email"] = dataframe["email"].apply(
            lambda x: self._get_email_provider(x)
        )
        dataframe["birthday"] = dataframe["birthday"].apply(
            lambda x: self._get_user_age(x)
        )
        return dataframe
