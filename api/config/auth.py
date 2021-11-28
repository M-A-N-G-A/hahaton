from flask_httpauth import HTTPTokenAuth
from itsdangerous import TimedJSONWebSignatureSerializer as JsonWebToken

jwt = JsonWebToken("top secret!", expires_in=3600)

refresh_jwt = JsonWebToken("telelelele", expires_in=7200)

auth = HTTPTokenAuth("Bearer")
