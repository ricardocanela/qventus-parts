import pytest
from django.urls import reverse
from parts.models import Part


@pytest.fixture
def create_parts(db):
    part1 = Part.objects.create(
        name="Test Part 1",
        sku="SKU123",
        description="Used for testing only",
        weight_ounces=10,
        is_active=True
    )
    part2 = Part.objects.create(
        name="Test Part 2",
        sku="SKU456",
        description="Testing part again for common word counting",
        weight_ounces=20,
        is_active=False
    )
    return [part1, part2]


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()


def test_list_parts(api_client, create_parts):
    url = reverse("part-list")
    response = api_client.get(url)
    assert response.status_code == 200
    assert len(response.data) == 2


def test_get_part_detail(api_client, create_parts):
    url = reverse("part-detail", args=[create_parts[0].id])
    response = api_client.get(url)
    assert response.status_code == 200
    assert response.data["sku"] == create_parts[0].sku

@pytest.mark.django_db
def test_create_part(api_client):
    url = reverse("part-list")
    data = {
        "name": "New Part",
        "sku": "SKU789",
        "description": "Brand new part for testing",
        "weight_ounces": 5,
        "is_active": True
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 201
    assert Part.objects.count() == 1


def test_update_part(api_client, create_parts):
    part = create_parts[0]
    url = reverse("part-detail", args=[part.id])
    data = {
        "name": "Updated Name",
        "sku": part.sku,
        "description": part.description,
        "weight_ounces": 999,
        "is_active": False
    }
    response = api_client.put(url, data, format="json")
    assert response.status_code == 200
    part.refresh_from_db()
    assert part.name == "Updated Name"
    assert part.weight_ounces == 999


def test_delete_part(api_client, create_parts):
    part = create_parts[0]
    url = reverse("part-detail", args=[part.id])
    response = api_client.delete(url)
    assert response.status_code == 204
    assert not Part.objects.filter(id=part.id).exists()


def test_common_words(api_client, create_parts):
    url = reverse("common-words")
    response = api_client.get(url)
    assert response.status_code == 200
    assert "testing" in response.data


def test_create_invalid_part_should_fail(api_client):
    url = reverse("part-list")
    data = {
        "name": "",
        "sku": "FAILSKU",
        "description": "Invalid",
        "weight_ounces": 5,
        "is_active": True
    }
    response = api_client.post(url, data, format="json")
    assert response.status_code == 400

def test_part_str(create_parts):
    part = create_parts[0]
    expected = f"{part.name} ({part.sku})"
    assert str(part) == expected
