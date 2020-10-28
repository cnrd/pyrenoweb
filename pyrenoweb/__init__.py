"""A Python Wrapper to communicate with RenoWeb API."""

from pyrenoweb.client import RenoWeb, RenoWebData
from pyrenoweb.errors import (
    InvalidApiKey,
    RequestError,
    ResultError,
    MunicipalityError,
)
from pyrenoweb.const import (
    TYPE_METAL_GLASS,
    TYPE_PAPER,
    TYPE_RESIDUAL,
)
