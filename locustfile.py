from locust import HttpUser, task


PREDICTION_DICTIONARY = {
        "CHAS": {"0": 0},
        "RM": {"0": 6.575},
        "TAX": {"0": 296.0},
        "PTRATIO": {"0": 15.3},
        "B": {"0": 396.9},
        "LSTAT": {"0": 4.98},
    }

WEB_SERVICE_ADDRESS = "https://flaskwebappproject.azurewebsites.net"


class QuickstartUser(HttpUser):
    @task
    def test_load_of_webapp(self):
        self.client.get(WEB_SERVICE_ADDRESS)

    @task
    def post(self):
        self.client.post("predict", json=PREDICTION_DICTIONARY)