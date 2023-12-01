import asyncio

from viam.module.module import Module
from viam.components.sensor import Sensor

from .co2meter import MySensor 

async def main():
    """This function creates and starts a new module, after adding all desired resources.
    Resources must be pre-registered.
    """

    module = Module.from_args()
    module.add_model_from_registry(Sensor.SUBTYPE, MySensor.MODEL)
    module.add_model_from_registry(Sensor.SUBTYPE, MySensor.MODEL_FAKE)
    await module.start()


if __name__ == "__main__":
    asyncio.run(main())
