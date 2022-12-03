import base64
import pycspr
from pycspr.types import CL_Key

# get account hash from public key 
# public key: 0125a6336791eba195c472a8b7dbcd256a6ecddf8863e586a3dfefe2581a5d672c
_ACCOUNT_KEY: bytes = bytes.fromhex("0125a6336791eba195c472a8b7dbcd256a6ecddf8863e586a3dfefe2581a5d672c")

# Account hash mapped from account key.
_ACCOUNT_HASH: bytes = pycspr.get_account_hash(_ACCOUNT_KEY)

print("account_hash => ",_ACCOUNT_HASH.hex())
itemKey  = base64.b64encode(b'\x00' + _ACCOUNT_HASH)
print("itemKey => ",itemKey.decode("utf-8"))

# get account hash directly
account_key=CL_Key.from_string('account-hash-2293223427d59ebb331ac2221c3fcd1b3656a5cb72be924a6cdc9d52cdb6db0f')
itemKey  = base64.b64encode(b'\x00' + account_key.identifier)
print("itemKey => ",itemKey.decode("utf-8"))