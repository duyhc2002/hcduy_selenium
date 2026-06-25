import pytest
from utils.api_helper import APIHelper
from utils.config_reader import ConfigReader

class TestDummyJSONProductsAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_helper = APIHelper(base_url=ConfigReader.get_api_base_url())
        yield
        self.api_helper.close_session()

    @pytest.mark.get
    def test_get_product(self):
        response = self.api_helper.get("products/1")

        assert response.status_code == 200
        product = response.json()
        assert product["id"] == 1
        assert product["title"] == "Essence Mascara Lash Princess"