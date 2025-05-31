from flask_api import app

def test_prediction():
    with app.test_client() as client:
        response = client.post('/predict', json={'age': 30})
        assert response.status_code == 200
        assert 'predicted_salary' in response.get_json()
