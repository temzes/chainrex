# WALLET
from web3 import Account as Ethereum

# EXTRA
Ethereum.enable_unaudited_hdwallet_features()

# MAIN
def create(strength: int) -> dict:
    try:
        if strength in [12, 15, 18, 21, 24]:
            account, mnemonic = Ethereum.create_with_mnemonic(num_words = strength)
            #
            privatekey = account._private_key.hex()
            address = account.address
            #
            return {"ethereum": {"mnemonic": mnemonic, "privatekey": privatekey, "address": address}}
        else:
            return {"error": f"Mnemonic length cant be {strength}"}
    except Exception as CreateAccountError:
        raise SystemError(CreateAccountError)
