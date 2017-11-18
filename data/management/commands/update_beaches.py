import json
import os

from django.core.management.base import BaseCommand, CommandError
from fastkml import kml
from requests import post, get, delete

from data.views import authentication_headers

class Command(BaseCommand):
    url = "https://dapi.microshare.io/share/com.hackforthesea.global.location/"

    def handle(self, *args, **options):
        headers = authentication_headers()

        response = get(self.url, headers=headers)
        items = response.json()['objs']

        for item in items:
            delete(self.url + item['id'], headers=headers)

        with open("./data/management/beaches.kml") as f:
            k = kml.KML()
            k.from_string(f.read())
            features = list(k.features())
            for feature in features[0].features():
                beach = {
                    "name": feature.name,
                    "description": feature.description,
                    "geometry": {
                        "type": "point",
                        "coordinates": [feature.geometry.x, feature.geometry.y]
                    }
                }

                response = post(self.url + 'tags/beach/massachusetts/united states', json.dumps(beach), headers=headers)
                print(response.text)

        return "Beaches processed!"

