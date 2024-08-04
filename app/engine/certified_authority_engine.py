# # Next Dev : Trying to make a CA with cryptography library

# from cryptography.hazmat.primitives.asymmetric import rsa
# from cryptography.hazmat.primitives import serialization
# # from cryptography.hazmat.primitives.x509 import Name, NameAttribute
# # from cryptography.hazmat.primitives.x509 import NameOID



# # Generate a private key for CA
# private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
# )

# # Save the private key to a file
# with open("ca_key.pem", "wb") as f:
#     f.write(private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.TraditionalOpenSSL,
#         encryption_algorithm=serialization.NoEncryption()
#     ))


# # Generate a private key for CA
# private_key = rsa.generate_private_key(
#     public_exponent=65537,
#     key_size=2048,
# )

# # Save the private key to a file
# with open("ca_key.pem", "wb") as f:
#     f.write(private_key.private_bytes(
#         encoding=serialization.Encoding.PEM,
#         format=serialization.PrivateFormat.TraditionalOpenSSL,
#         encryption_algorithm=serialization.NoEncryption()
#     ))


# # Create the subject name
# subject = Name([
#     NameAttribute(NameOID.COUNTRY_NAME, u"US"),
#     NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
#     NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
#     NameAttribute(NameOID.ORGANIZATION_NAME, u"Document Signer"),
#     NameAttribute(NameOID.COMMON_NAME, u"docsigner.example.com"),
# ])

# # Create the certificate
# doc_cert = CertificateBuilder().subject_name(subject).issuer_name(subject).public_key(doc_signing_key.public_key()).serial_number(2).not_valid_before(datetime.utcnow()).not_valid_after(datetime.utcnow() + timedelta(days=365)).add_extension(BasicConstraints(ca=False, path_length=None), critical=True).sign(doc_signing_key, hashes.SHA256())

# # Save the certificate
# with open("doc_signing_cert.pem", "wb") as f:
#     f.write(doc_cert.public_bytes(Encoding.PEM))

    