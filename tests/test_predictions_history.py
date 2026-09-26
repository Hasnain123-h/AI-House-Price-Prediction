from fastapi.testclient import TestClient
from api.main import app
client = TestClient(app)
def test_predictions_history():
    response = client.get(
        "/predictions"
    )
    assert response.status_code==200
    result = response.json()
    assert "predictions" in result
    
    assert isinstance(
        result["predictions"],
        list
    )