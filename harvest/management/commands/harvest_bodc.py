import json

from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand, CommandError
from requests import get, post

data_library_url = 'https://www.bodc.ac.uk/data/published_data_library/'

payload1 = {
    "payload": '{"outtype":"userhistory","brandid":"PDL","userhist":[{"subject":"PDL","predicate":"reuse","object":"WYsFZMXygnyvkPvyitiKwnmzgunjTHsx"}]}'
}

payload2 = {
    "payload": '{"outtype":"jsoncritvalscapnval","brandid":"PDL","searchoncriterion":[{"subject":"T6000024","predicate":"codnam_"},{"subject":"T6000024","predicate":"codval_"}],"userhist":[{"subject":"PDL","predicate":"savefor","object":"WYsFZMXygnyvkPvyitiKwnmzgunjTHsx"}],"summaryinfo":[{"subject":"T6000024","predicate":"boxes","object":"Author"},{"subject":"T6000025","predicate":"boxes","object":"Summary title"},{"subject":"T6000026","predicate":"boxes","object":"Publication date"},{"subject":"T6000027","predicate":"dates","object":"Temporal coverage"}],"colheader":[{"subject":"T6000029","predicate":"1","object":"value"},{"subject":"T6000030","predicate":"2","object":"value"},{"subject":"T6000026","predicate":"3","object":"value"},{"subject":"T6000027","predicate":"4","object":"value"},{"subject":"T6000031","predicate":"5","object":"value"}],"info4brandid":[{"subject":"type","predicate":"is","object":"likepdl"}],"sortcriterion":[{"subject":"T6000029","predicate":"sortpredicate","object":"value"},{"subject":"T6000029","predicate":"sortorder","object":"asc"}],"pageinfo":[{"subject":"pageinfo","predicate":"pagenum","object":"1"},{"subject":"pageinfo","predicate":"pagemax","object":"10"}],"searchtab":[{"subject":"selectedtab","predicate":"is","object":"T6000024typboxes"}],"helpinfo":[{"subject":"url","predicate":"is","object":""}]}'
}

payload3 = {
    "payload": '{"outtype":"jsptabres","brandid":"PDL","userhist":[{"subject":"PDL","predicate":"savefor","object":"WYsFZMXygnyvkPvyitiKwnmzgunjTHsx"}],"summaryinfo":[{"subject":"T6000024","predicate":"boxes","object":"Author"},{"subject":"T6000025","predicate":"boxes","object":"Summary title"},{"subject":"T6000026","predicate":"boxes","object":"Publication date"},{"subject":"T6000027","predicate":"dates","object":"Temporal coverage"}],"colheader":[{"subject":"T6000029","predicate":"1","object":"value"},{"subject":"T6000030","predicate":"2","object":"value"},{"subject":"T6000026","predicate":"3","object":"value"},{"subject":"T6000027","predicate":"4","object":"value"},{"subject":"T6000031","predicate":"5","object":"value"}],"info4brandid":[{"subject":"type","predicate":"is","object":"likepdl"}],"sortcriterion":[{"subject":"T6000029","predicate":"sortpredicate","object":"value"},{"subject":"T6000029","predicate":"sortorder","object":"asc"}],"pageinfo":[{"subject":"pageinfo","predicate":"pagenum","object":"1"},{"subject":"pageinfo","predicate":"pagemax","object":"10"}],"searchtab":[{"subject":"selectedtab","predicate":"is","object":"T6000024typboxes"}],"helpinfo":[{"subject":"url","predicate":"is","object":""}]}'
}

class Command(BaseCommand):
    help = 'Harvest BODC DOIs'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_id', nargs='+', type=int)

    def handle(self, *args, **options):
        try:
            data_library_json1 = post(data_library_url, payload1)
            data_library_json2 = post(data_library_url, payload2)
            data_library_json3 = post(data_library_url, payload3)
            soup = BeautifulSoup(data_library_json3.text, 'html.parser')

            for tr in soup.select('#tabofres tr')[1:]:
                tds = tr.select('td')
                print({tds[1].text)

        except Exception as e:
            raise CommandError('%s' % e)

        self.stdout.write('Not Implemented')