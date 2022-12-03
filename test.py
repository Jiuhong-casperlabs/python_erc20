import base64
import pycspr


# public key: 0125a6336791eba195c472a8b7dbcd256a6ecddf8863e586a3dfefe2581a5d672c
_ACCOUNT_KEY: bytes = bytes.fromhex("0125a6336791eba195c472a8b7dbcd256a6ecddf8863e586a3dfefe2581a5d672c")

# Account hash mapped from account key.
_ACCOUNT_HASH: bytes = pycspr.get_account_hash(_ACCOUNT_KEY)

print("account_hash", _ACCOUNT_HASH.hex())
itemKey  = base64.b64encode(b'\x00' + _ACCOUNT_HASH)
print("itemKey",itemKey.decode("utf-8"))
