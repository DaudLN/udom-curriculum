from rest_framework.renderers import JSONRenderer


class CustomJSONRenderer(JSONRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # Call the parent class's render method to get the JSON string
        json_string = super().render(data, accepted_media_type, renderer_context)

        # Remove the DRF header from the JSON string
        header = '{"detail":'
        if json_string.startswith(header):
            json_string = json_string[len(header) :]
            json_string = json_string[:-2]

        # Return the modified JSON string
        return json_string
