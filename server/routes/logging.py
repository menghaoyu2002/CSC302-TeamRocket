"""The module for logging requests"""
import datetime
import time
from typing import Tuple, List
from flask import Blueprint, current_app, g, request


logging_blueprint = Blueprint("logger", __name__)


@logging_blueprint.before_app_request
def log_request_start():
    """Start a timer for how long the request takes"""
    g.start = time.time()
    now = time.time()
    timestamp = datetime.datetime.fromtimestamp(now).isoformat()

    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)

    log_params = [
        ('method', request.method),
        ('path', request.path),
        ('time', timestamp),
        ('ip', ip_address),
        ('host', host),
        ('params', args),
        ('body', request.get_json(silent=True)),
    ]

    current_app.logger.info('received request: ' +
                            parse_tuples_to_line(log_params))


@logging_blueprint.after_app_request
def log_request_end(response):
    """Log every request and the data passed in each request"""
    now = time.time()
    duration = round(now - g.start, 2)
    timestamp = datetime.datetime.fromtimestamp(now).isoformat()

    ip_address = request.headers.get('X-Forwarded-For', request.remote_addr)
    host = request.host.split(':', 1)[0]
    args = dict(request.args)

    log_params = [
        ('method', request.method),
        ('path', request.path),
        ('status', response.status_code),
        ('duration', duration),
        ('time', timestamp),
        ('ip', ip_address),
        ('host', host),
        ('params', args),
        ('body', request.get_json(silent=True)),
        ('response', response.get_json(silent=True))
    ]

    request_id = request.headers.get('X-Request-ID')
    if request_id:
        log_params.append(('request_id', request_id))

    current_app.logger.info('completed request: ' +
                            parse_tuples_to_line(log_params))

    return response


def parse_tuples_to_line(log_params: List[Tuple[str, any]]):
    """Parse the log parameters into a string of key value pairs"""
    parts = []
    for name, value in log_params:
        parts.append(f"{name}={value}")
    return " ".join(parts)
