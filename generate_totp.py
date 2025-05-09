import hmac, hashlib, time, struct, base64

def generate_totp(secret, digits=10, timestep=30):
    T = int(time.time()) // timestep
    key = secret.encode()
    msg = struct.pack(">Q", T)
    h = hmac.new(key, msg, hashlib.sha512).digest()
    o = h[-1] & 0x0F
    code = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % (10 ** digits)
    return f"{code:0{digits}}"

email = "yoonyoon.mu@gmail.com"
secret = email + "HENNGECHALLENGE004"

# Generate TOTP
otp = generate_totp(secret)
auth_string = f"{email}:{otp}"
auth_token = base64.b64encode(auth_string.encode()).decode()
print("Authorization: Basic", auth_token)
