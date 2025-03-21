# Easy OIDC Flow

This python library is designed to be an easy drop in which handles OIDC authentication,
authorization, and the OAuth flow.

## Example Implementation
```python
from flask import Flask, request
from easy_oidc_flow import EasyOIDCFlow

app = EasyOIDCFlow(Flask(__name__))

@app.route("/")
def main():
  return f"hello {request.user_data["email"]}!"

if __name__ in "__main__":
  app.run(host="0.0.0.0", port=8000, debug=True)
```


## Quickstart
Note: This example uses `uv` but this package can be used via native `pip` or other package managers which work with pypi.

0) To get started, install the package:
```
uv run pip install easy_oidc_flow
```

1) Create a .env file using the .env.template file as a template. Populate with your OAuth Client details (see below)

2) Run the example server implementation with the following:

```bash
uv run --env-file=.env .\example_server.py
```

3) Navigate to `http://localhost:8000/`
4) Follow through the OAuth flow
5) Congrats! You are now successfully authorized.

## IDP Configuration

### Google Cloud Platform
0) Create a GCP Project
1) Navigate to https://console.cloud.google.com/auth/clients/
2) Create a Web Application OAuth Client ID. Make sure to configure the redirect URI to `http://localhost:8000/callback`

3) Download the OAuth client id .json file
4) Copy .env to .env.template and fill out the client id and client secret from the downloaded OAuth .json file
5) Delete the .json file from your system

![Google Cloud Platform Identity Platform Client ID creation](gcp_oauth_client_id.png)

## Additional Details
This Flask context wrapper overrides the following REST routes:
`/login`
`/callback`

Make sure that your flask app doesn't define these routes, otherwise an error will be thrown.

## Contributing

Please open an issue or pull request if you find any bugs, have a feature request, or would like to contribute!

## PyPi

https://pypi.org/project/easy_oidc_flow/

## References

https://developers.google.com/identity/openid-connect/openid-connect#discovery