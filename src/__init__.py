from viam.components.sensor import Sensor
from viam.resource.registry import Registry, ResourceCreatorRegistration
from .co2meter import MySensor


Registry.register_resource_creator(Sensor.SUBTYPE, MySensor.MODEL, ResourceCreatorRegistration(MySensor.new))
Registry.register_resource_creator(Sensor.SUBTYPE, MySensor.MODEL_FAKE, ResourceCreatorRegistration(MySensor.new_fake))
