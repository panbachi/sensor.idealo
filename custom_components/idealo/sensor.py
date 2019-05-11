"""
A platform to receive prices of a product from idealo.

For more details about this platform, please refer to the documentation at
https://github.com/panbachi/sensor.idealo/
"""
import logging
from datetime import timedelta

import voluptuous as vol
import requests

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.util import Throttle
from homeassistant.helpers.entity import Entity
from homeassistant.const import CONF_NAME

_LOGGER = logging.getLogger(__name__)

CONF_DESCRIPTION = 'description'
CONF_PRODUCT_ID = 'product_id'
CONF_LOCALE = 'locale'

DEFAULT_SCAN_INTERVAL = timedelta(seconds=300)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Required(CONF_NAME): cv.string,
    vol.Required(CONF_PRODUCT_ID): cv.positive_int,
    vol.Optional(CONF_DESCRIPTION, default='Price'): cv.string,
    vol.Optional(CONF_LOCALE, default='DE'): vol.In(
        ['AT',
         'DE',
         'ES',
         'FR',
         'IT',
         'UK']),
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the Idealo sensor."""
    name = config.get(CONF_NAME)
    description = config.get(CONF_DESCRIPTION)
    product_id = config.get(CONF_PRODUCT_ID)
    domain = config.get(CONF_LOCALE)

    add_entities([IdealoAPI(name, description, product_id, domain)],
True)


class IdealoAPI(Entity):
    """Implementation of IdealoAPI"""

    def __init__(self, name, description, product_id, domain):
        """Initialize the sensor."""

        self._name = name
        self._description = description
        self._product_id = product_id
        self._unit_of_measurement = '€'
        self._domain = domain.lower()
        self._locale = domain

        if(domain == 'UK'):
            self._unit_of_measurement = '£'
            self._domain = 'co.uk'
            

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        if(self._data):
            return self._data['data'][-1]['y']

        return None

    @property
    def icon(self):
        """Return the icon for the frontend."""
        return 'mdi:coin'

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        attrs = {'description': self._description,
                 'product_id': self._product_id,
                 'locale': self._locale
                }

        return attrs

    @Throttle(DEFAULT_SCAN_INTERVAL)
    def update(self):
        response = requests.get('https://www.idealo.' + self._domain + '/offerpage/pricechart/api/' + str(self._product_id) + '?period=P1M');

        self._data = response.json()
        _LOGGER.info(self._data)

