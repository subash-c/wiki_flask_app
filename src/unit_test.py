import pytest
from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['DEBUG'] = False  # Disable debug mode
    with app.test_client() as client:
        yield client

# Test Case 1 - Get top frequent words
def test_word_frequency_analysis(client):
    response = client.get('word-frequencies?topic=elonmusk&n=5')
    data = response.get_json()
    assert response.status_code == 200
    assert 'topic' in data
    assert 'frequent_words' in data

# Test Case 2 - Get search history
def test_search_history_endpoint(client):
    response = client.get('/search_history')
    data = response.get_json()
    assert response.status_code == 200
    assert 'search_history' in data


if __name__ == '__main__':
    pytest.main()
