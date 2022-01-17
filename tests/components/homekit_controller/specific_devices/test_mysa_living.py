"""Make sure that Mysa Living is enumerated properly."""

from homeassistant.components.climate import SUPPORT_TARGET_TEMPERATURE
from homeassistant.components.light import SUPPORT_BRIGHTNESS
from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import PERCENTAGE, TEMP_CELSIUS

from tests.components.homekit_controller.common import (
    DeviceTestInfo,
    EntityTestInfo,
    assert_devices_and_entities_created,
    setup_accessories_from_file,
    setup_test_accessories,
)


async def test_mysa_living_setup(hass):
    """Test that the accessory can be correctly setup in HA."""
    accessories = await setup_accessories_from_file(hass, "mysa_living.json")
    await setup_test_accessories(hass, accessories)

    await assert_devices_and_entities_created(
        hass,
        DeviceTestInfo(
            unique_id="00:00:00:00:00:00",
            name="Mysa-85dda9",
            model="v1",
            manufacturer="Empowered Homes Inc.",
            sw_version="2.8.1",
            hw_version="",
            serial_number="AAAAAAA000",
            devices=[],
            entities=[
                EntityTestInfo(
                    entity_id="climate.mysa_85dda9",
                    friendly_name="Mysa-85dda9",
                    unique_id="homekit-AAAAAAA000-20",
                    supported_features=SUPPORT_TARGET_TEMPERATURE,
                    capabilities={
                        "hvac_modes": ["off", "heat", "cool", "heat_cool"],
                        "max_temp": 35,
                        "min_temp": 7,
                    },
                    state="off",
                ),
                EntityTestInfo(
                    entity_id="sensor.mysa_85dda9_current_humidity",
                    friendly_name="Mysa-85dda9 - Current Humidity",
                    unique_id="homekit-AAAAAAA000-aid:1-sid:20-cid:27",
                    unit_of_measurement=PERCENTAGE,
                    capabilities={"state_class": SensorStateClass.MEASUREMENT},
                    state="40",
                ),
                EntityTestInfo(
                    entity_id="sensor.mysa_85dda9_current_temperature",
                    friendly_name="Mysa-85dda9 - Current Temperature",
                    unique_id="homekit-AAAAAAA000-aid:1-sid:20-cid:25",
                    unit_of_measurement=TEMP_CELSIUS,
                    capabilities={"state_class": SensorStateClass.MEASUREMENT},
                    state="24.1",
                ),
                EntityTestInfo(
                    entity_id="light.mysa_85dda9",
                    friendly_name="Mysa-85dda9",
                    unique_id="homekit-AAAAAAA000-40",
                    supported_features=SUPPORT_BRIGHTNESS,
                    capabilities={"supported_color_modes": ["brightness"]},
                    state="off",
                ),
            ],
        ),
    )
