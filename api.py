import requests


BASE_URL = "https://challenge.crossmint.io/api/"
CANDIDATE_ID = "88937ad5-e903-404f-9dfe-e950243fd234"


class APIHelper(object):
    headers = {"Content-Type": "application/json"}
    input_data = {"candidateId": CANDIDATE_ID}

    @classmethod
    def generate_input_data(cls, **kwargs):
        """
        Generates the input data for post request api call from variable list of arguments
        :param kwargs:
        :return:
        """
        additional_data = {}
        for field, value in kwargs.items():
            additional_data[field] = value
        return {**additional_data, **cls.input_data}

    @classmethod
    def generate_get_request(cls):
        """
        Generates the get request to retrieve the value for each cell in the goal matrix
        :return: Response
        """
        try:
            return requests.get(
                BASE_URL + "map/" + CANDIDATE_ID + "/goal", headers=cls.headers
            ).json()
        except requests.exceptions.HTTPError as err:
            raise SystemError(err)

    @classmethod
    def generate_post_request(cls, url, input_data):
        """
        Generates the post request to create the astral object with proper color or direction if applicable
        :param url: str
        :param input_data: dict
        :return: Response
        """
        try:
            return requests.post(url, json=input_data, headers=cls.headers)
        except requests.exceptions.HTTPError as err:
            raise SystemError(err)


class PolyanetGenerator(APIHelper):
    type = "polyanets"

    @classmethod
    def generate_astral_object(cls, **kwargs):
        input_data = super().generate_input_data(**kwargs)
        super().generate_post_request(BASE_URL + cls.type, input_data)


class SoloonGenerator(APIHelper):
    type = "soloons"

    @classmethod
    def generate_astral_object(cls, **kwargs):
        input_data = super().generate_input_data(**kwargs)
        super().generate_post_request(BASE_URL + cls.type, input_data)


class ComethGenerator(APIHelper):
    type = "comeths"

    @classmethod
    def generate_astral_object(cls, **kwargs):
        input_data = super().generate_input_data(**kwargs)
        super().generate_post_request(BASE_URL + cls.type, input_data)


ASTRAL_OBJECT_SELECTOR = {
    "polyanet": {"generator_class": PolyanetGenerator, "attribute": None},
    "soloon": {"generator_class": SoloonGenerator, "attribute": "color"},
    "cometh": {"generator_class": ComethGenerator, "attribute": "direction"},
}
