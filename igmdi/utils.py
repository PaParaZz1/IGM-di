import json
import yaml


def pretty_print(x):
    cleaned = json.dumps(x)
    return yaml.safe_dump(json.loads(cleaned), default_flow_style=False)
