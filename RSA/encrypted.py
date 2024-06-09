import rsa


with open("public.pem","rb") as f:
    public_key=rsa.PublicKey.load_pkcs1(f.read())


with open("private.pem","rb") as f:
    private_key=rsa.PrivateKey.load_pkcs1(f.read())

# Write the message that needs to be encrypted

    message = "i queen"

    encrypted_message= rsa.encrypt(message.encode(),public_key)

    with open("encryp_Mes87","wb") as f:
        f.write(encrypted_message)