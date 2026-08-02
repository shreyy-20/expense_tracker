#!/bin/sh
set -e

# Resolve API upstream URL with a default for docker-compose
: "${API_UPSTREAM_URL:=http://backend:8000}"

# Render the nginx config template
envsubst '${API_UPSTREAM_URL}' < /etc/nginx/conf.d/default.conf.template > /etc/nginx/conf.d/default.conf

# Verify nginx config is valid
nginx -t

exec "$@"

