
from django.template.loader import render_to_string

class BaseBackend(object):
    """
    The base backend.
    """
    def __init__(self, label):
        self.label = label
    
    def can_send(self, user, notice_type):
        """
        Determines whether this backend is allowed to send a notification to
        the given user and notice_type.
        """
        return False
    
    def deliver(self, recipient, notice_type, extra_context):
        """
        Deliver a notification to the given recipient.
        """
        raise NotImplemented()
    
    def get_formatted_messages(self, formats, label, context):
        """
        Returns a dictionary with the format identifier as the key. The values are
        are fully rendered templates with the given context.
        """
        format_templates = {}
        for format in formats:
            # conditionally turn off autoescaping for .txt extensions in format
            if format.endswith(".txt"):
                context.autoescape = False
            format_templates[format] = render_to_string((
                "notification/%s/%s" % (label, format),
                "notification/%s" % format), context_instance=context)
        return format_templates
