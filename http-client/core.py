"""Core module."""

class Processor:
    def process(self, data):
        """Process the input data."""
        return {{"status": "ok", "data": data}}

    def validate(self, data):
        """Validate data format."""
        return isinstance(data, dict)