from django.http import HttpResponse
from django.conf import settings

class IPBlockMiddleware:
    """
    Middleware to block access for specific IP addresses.
    """
    def __init__(self, get_response):
        self.get_response = get_response
        # Initialize the list of blocked IPs from settings
        self.blocked_ips = getattr(settings, 'BLOCKED_IPS', [])

    def __call__(self, request):
        # Get the IP address of the request
        ip_address = self.get_client_ip(request)
        
        # Check if the IP address is in the blocked list
        if ip_address in self.blocked_ips:
            # Return a custom response indicating the IP is blocked
            return HttpResponse("You are blocked from accessing this site.", status=403)
        
        # Process the request as usual if IP is not blocked
        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        """
        Get the client IP address from the request, handling headers that may be set by a proxy.
        """
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
