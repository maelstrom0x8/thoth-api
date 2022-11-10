import pytest

from api import models

@pytest.mark.django_db
def test_entries_have_unique_creation_dates():
    e1 = models.LogEntry.objects.create(subject='', body='')
    e2 = models.LogEntry.objects.create(subject='', body='')

    assert e1.created != e2.created
