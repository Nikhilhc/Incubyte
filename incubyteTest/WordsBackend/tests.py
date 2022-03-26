from django import urls
from django.contrib.auth import get_user_model
import pytest
import json
import requests
from .models import Words

@pytest.mark.django_db
@pytest.mark.parametrize('param', [
    ('WordsList'),
])
def test_render_views(client, param):
    temp_url = urls.reverse(param)
    print(temp_url)
    resp = client.get(temp_url)
    assert resp.status_code == 200

@pytest.mark.django_db
def test_add_records(client):
    add_url = urls.reverse('WordsList')
    resp = requests.post('http://127.0.0.1:8001/api/words/', {'words':'test1'})
    resp_json = json.loads(resp.content)
    assert resp.status_code==201

@pytest.mark.django_db
def test_get_delete_records(client):
    add_url = urls.reverse('WordsList')
    resp = requests.delete('http://127.0.0.1:8001/api/words/6')
    assert resp.status_code==204


@pytest.mark.django_db
def test_get_delete_records_failed(client):
    add_url = urls.reverse('WordsList')
    resp = requests.delete('http://127.0.0.1:8001/api/words/6')
    assert resp.status_code==404

@pytest.mark.django_db
def test_update_record(client):
    count = Words.objects.count()
    add_url = urls.reverse('WordsList')
    resp = requests.patch('http://127.0.0.1:8001/api/words/7',{'words':'testtemp'})
    assert resp.status_code==201


