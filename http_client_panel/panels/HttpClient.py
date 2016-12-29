# -*- coding: utf-8 -*-
import functools

from vcr import VCR

from debug_toolbar.panels import Panel
from vcr.cassette import CassetteContextDecorator, Cassette


class MemoryCassette(Cassette):
    """A simple memory cassette"""
    _records = {}

    @classmethod
    def clear_records(cls, path):
        del cls._records[path]

    @classmethod
    def save_cassette(cls, path, data, serializer=None):
        cls._records[path] = zip(data["requests"], data["responses"])

    @classmethod
    def load_cassette(cls, path, serializer=None):
        return cls._records.get(path, ([], []))

    def _save(self, force=False):
        if force or self.dirty:
            self.save_cassette(
                self._path,
                self._as_dict(),
                serializer=self._serializer
            )
            self.dirty = False

    def _load(self):
        try:
            requests, responses = self.load_cassette(
                self._path,
                serializer=self._serializer
            )
            for request, response in zip(requests, responses):
                self.append(request, response)
            self.dirty = False
            self.rewound = True
        except IOError:
            pass

    def __contains__(self, request):
        """Return whether or not a request has been stored"""
        for index, response in self._responses(request):
            if self.play_counts[index] == 0:
                return True
        return False


class MemoryVCR(VCR):
    def _use_cassette(self, with_current_defaults=False, **kwargs):
        if with_current_defaults:
            config = self.get_merged_config(**kwargs)
            return MemoryCassette.use(**config)
        # This is made a function that evaluates every time a cassette
        # is made so that changes that are made to this VCR instance
        # that occur AFTER the `use_cassette` decorator is applied
        # still affect subsequent calls to the decorated function.
        args_getter = functools.partial(self.get_merged_config, **kwargs)
        return MemoryCassette.use_arg_getter(args_getter)


memory_vcr = MemoryVCR(
    record_mode="all",
    decode_compressed_response=True,
)


class HttpClientPanel(Panel):
    """
    A panel to display http request make by server.
    http request record is base on vcrpy, which could record request made by
    requests, aiohttp, urllib3, tornado, urllib2, boto, boto3
    """
    name = "HTTPClient"
    title = "HTTP Client"
    template = 'debug_toolbar_http_client.html'
    has_content = True

    def process_view(self, request, view_func, view_args, view_kwargs):
        args = (request, ) + view_args
        # with CassetteContextDecorator(
        #         MemoryCassette,
        #         lambda: {"path": id(self),
        #                  "record_mode": "all"}):
        with memory_vcr.use_cassette(path=str(id(self))):
            return view_func(*args, **view_kwargs)

    def generate_stats(self, request, response):
        http_records = MemoryCassette.load_cassette(str(id(self)))
        self.record_stats({'request_records': http_records})
        return response
