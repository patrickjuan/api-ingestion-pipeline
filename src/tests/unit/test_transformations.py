from src.transformer import Transformer

transformer = Transformer()


def test_anonymize_data_should_pass():
    input = [
        {
            "id": 1,
            "firstname": "Kaleb",
            "lastname": "Eichmann",
            "email": "pouros.kurtis@farrell.info",
            "phone": "+3057533611691",
            "birthday": "1924-10-18",
            "gender": "male",
            "address": {
                "id": 0,
                "street": "840 Watsica Shoals",
                "streetName": "Weber Views",
                "buildingNumber": "40534",
                "city": "Murazikview",
                "zipcode": "56839-1871",
                "country": "Panama",
                "county_code": "AE",
                "latitude": 42.52815,
                "longitude": 79.586848,
            },
            "website": "http://feeney.com",
            "image": "http://placeimg.com/640/480/people",
        }
    ]
    expected_output = [
        {
            "id": "****",
            "firstname": "****",
            "lastname": "****",
            "email": "pouros.kurtis@farrell.info",
            "phone": "****",
            "birthday": "1924-10-18",
            "gender": "****",
            "address_id": "****",
            "address_street": "****",
            "address_streetName": "****",
            "address_buildingNumber": "****",
            "address_city": "****",
            "address_zipcode": "****",
            "address_country": "Panama",
            "address_county_code": "****",
            "address_latitude": "****",
            "address_longitude": "****",
            "website": "****",
            "image": "****",
        }
    ]
    output = transformer.anonymize_data(input)
    assert output == expected_output
