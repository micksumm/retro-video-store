from app.models.rental import Rental

def test_create_rental(client, one_customer, one_video):
    # Act
    response = client.post("/rentals/check-out", json={
        "customer_id": 1,
        "video_id": 1
    })

    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body["customer_id"] == 1
    assert response_body["video_id"] == 1
    assert response_body["videos_checked_out_count"] == 1
    assert response_body["available_inventory"] == 9