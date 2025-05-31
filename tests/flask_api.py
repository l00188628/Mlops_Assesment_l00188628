from flask_api import app

def test_prediction_missing_age():
    with app.test_client() as client:
        response = client.post('/predict', json={})
        assert response.status_code == 400 or response.status_code == 422
