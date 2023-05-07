import logging

from bleak import BleakScanner
from bleak.backends.client import BLEDevice

from ._constants import STEINEL_GMBH_COMPANY_ID

_LOGGER = logging.getLogger(__name__)

async def discover() -> list[BLEDevice]:
    """Discover all Steinel devices in range.

    :return: A list of all discovered Steinel devices.
    """

    # Discover all devices in range
    device_list = await BleakScanner.discover(return_adv=True)

    # Filter out all devices that aren't Steinel devices
    discovered = []
    for device, advertivement in device_list.values():
        if STEINEL_GMBH_COMPANY_ID in advertivement.manufacturer_data:
            _LOGGER.debug("discovered device at %{device}")
            discovered.append(device)
    return discovered
