from src.extractor import ExtractData
from src.transformer import Transformer
from src.loader import Loader
import pandas as pd


def main():
    try:
        extractor = ExtractData()
        transformer = Transformer()
        loader = Loader()

        raw_data = extractor.extract_data()
        anonymized_data = transformer.anonymize_data(raw_data)

        dataframe = pd.DataFrame(anonymized_data)

        data_generalizated = transformer.data_generalization(dataframe)
        loader.load_data(data_generalizated)
        print("Pipeline executed with success!")
    except Exception as err:
        print("Pipeline failed to extract data", {"error": err})
