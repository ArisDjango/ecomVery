import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AQGuVJDM2C6FHsmZ3cLoIjRNADAl_BtYbmerIbd1XVL2hHSyTqq8ufBeC4uFCRhVzbI2RCEPvhm2-nRC"
        self.client_secret = "EBOnbrtY53JtAGDj9g-cXRR2YtCym7_eJd6aZfMyijz_G7zWKcULRqREbcowOlHO8MFG3BCMVUEkwMRg"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)