from dataclasses import dataclass


@dataclass
class EndpointConfig:
    endpoint_prefix: str = "/api"
    map_uuid_to_id: bool = True
