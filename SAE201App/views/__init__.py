import typing

from django.shortcuts import render

if typing.TYPE_CHECKING:
    from django.http import HttpRequest


def ludotheque(request: "HttpRequest"):
    return render(request, "index.html")
