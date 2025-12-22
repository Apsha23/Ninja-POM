import requests

def test_get_posts():
    url = "https://jsonplaceholder.typicode.com/posts"

    response_data = requests.get(url)
    assert response_data.status_code == 200

    data = response_data.json()
    assert isinstance(data, list)

    assert "userId" in data[0]
    assert "id" in data[0]
    assert "title" in data[0]
    assert "body" in data[0]
    print(response_data)