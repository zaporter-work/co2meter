import asyncio
from typing import Any, ClassVar, Dict, Mapping, Optional
from viam.components.sensor import Sensor
from viam.proto.app.robot import ComponentConfig
from viam.proto.common import ResourceName
from viam.resource.base import ResourceBase
from viam.resource.types import Model, ModelFamily
import co2meter as co2

class MySensor(Sensor):
    MODEL: ClassVar[Model] = Model(ModelFamily("zack", "co2meter"), "v1")
    MODEL_FAKE: ClassVar[Model] = Model(ModelFamily("zack", "co2meter"), "v1-fake")

    @classmethod
    def new(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        sensor = cls(config.name)
        sensor.mon = co2.CO2monitor()
        sensor.is_fake = False
        print(sensor.mon.info)
        return sensor

    @classmethod
    def new_fake(cls, config: ComponentConfig, dependencies: Mapping[ResourceName, ResourceBase]):
        sensor = cls(config.name)
        sensor.is_fake = True
        print(sensor.mon.info)
        return sensor

    async def get_readings(self, extra: Optional[Dict[str, Any]] = None, **kwargs) -> Mapping[str, Any]:
        if self.is_fake:
            return {"ppm":450,"temp":20.0}
        else:
            data = self.mon.read_data()
            return {"ppm":data[1], "temp":data[2]}

async def main():
    co2mon=MySensor(name="wifi")
    signal = await co2mon.get_readings()
    print(signal)

if __name__ == '__main__':
    asyncio.run(main())
