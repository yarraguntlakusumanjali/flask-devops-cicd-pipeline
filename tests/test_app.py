from app import create_app

def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()

def test_home_page():
    response = client().get("/")
    assert response.status_code == 200
    assert b"DevOps Demo" in response.data

def test_health_endpoint():
    response = client().get("/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "healthy"

def test_info_endpoint():
    response = client().get("/api/info")
    assert response.status_code == 200
    assert response.get_json()["version"] == "1.0.0"
