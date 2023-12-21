from src.contants.api_contants import APIContants, BASE_URL, base_url


def test_crud(url_direct_func=None):
    print(BASE_URL)

    url_direc_func = base_url()
    print(url_direct_func)

    url_class = APIContants.base_url()
    print(url_class)