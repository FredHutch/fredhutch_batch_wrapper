"REST client"

import boto3
import botocore
import requests

class ClientError(Exception):
    """
    An exception to throw if the wrapper returned an error.
    We expect that the wrapper will return a dict with fields
    'error' (the error text) and 'exception' (the fully qualified
    name of the exception class).
    """
    fmt = """Wrapper threw an error.
Exception: {exception}
Message: {error}
"""
    def __init__(self, **kwargs):
        msg = self.fmt.format(**kwargs)
        Exception.__init__(self, msg)
        self.kwargs = kwargs
        print("hooha")

SERVER_ENDPOINT = "http://localhost:5000" # FIXME TODO CHANGEME update this!

class Client(object):
    "REST client"

    def __init__(self):
        session = boto3.Session()
        credentials = session.get_credentials()
        if credentials is None:
            raise botocore.exceptions.NoCredentialsError()
        credentials = credentials.get_frozen_credentials()
        self.access_key = credentials.access_key
        self.secret_key = credentials.secret_key



    def post_request(self, endpoint, **kwargs):
        "post a request"
        endpoint_url = "{}/{}".format(SERVER_ENDPOINT, endpoint)
        res = requests.post(endpoint_url, json=kwargs,
                            auth=requests.auth.HTTPBasicAuth(self.access_key,
                                                             self.secret_key))
        if res.status_code != 200:
            raise ClientError(**res.json())
        return res.json()

    def submit_job(self, **kwargs):
        "submit a job"
        return self.post_request("submit_job", **kwargs)


    def terminate_job(self, **kwargs):
        "terminate a job"
        return self.post_request("terminate_job", **kwargs)


    def cancel_job(self, **kwargs):
        "cancel a job"
        return self.post_request("cancel_job", **kwargs)
