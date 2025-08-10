#!/usr/bin/env python3
from Crypto.Util.number import *
import gmpy2, binascii


# EXTENDED EUCLIDEAN ALGORITHM
def compute_private_key(e, p, q) -> int:
    phi_n = (p - 1) * (q - 1)
    d = pow(e, -1, phi_n)
    
    return d

def decrypt_secret(secret, d, n):
    # Step 1: Convert hex string back to bytes
    print("Step 1: Converting hex to bytes...")
    try:
        # Remove the b' prefix and ' suffix if present, then convert
        if isinstance(secret, bytes):
            ciphertext_hex = secret.decode('utf-8')
        else:
            ciphertext_hex = secret
            
        ciphertext_bytes = binascii.unhexlify(ciphertext_hex)
        print(f"Ciphertext bytes length: {len(ciphertext_bytes)}\n")
        
    except Exception as e:
        print(f"Error converting hex: {e}\n")
        
        return
    
    # Step 2: Convert bytes to large integer
    print("Step 2: Converting bytes to integer...")
    ciphertext_int = bytes_to_long(ciphertext_bytes)
    print(f"Ciphertext as integer: {ciphertext_int}\n")
    
    # Step 3: RSA decryption (ciphertext^d mod n)
    print("Step 3: Performing RSA decryption...")
    decrypted_int = pow(ciphertext_int, d, n)
    print(f"Decrypted integer: {decrypted_int}\n")
    
    # Step 4: Convert integer back to bytes
    print("Step 4: Converting integer to bytes...")
    try:
        decrypted_bytes = long_to_bytes(decrypted_int)
        print(f"Decrypted bytes: {decrypted_bytes}\n")
        
    except Exception as e:
        print(f"Error converting to bytes: {e}\n")
        
        return
    
    # Step 5: Convert bytes to readable text
    print("Step 5: Converting bytes to text...")
    try:
        flag = decrypted_bytes.decode('utf-8')
        print(f"DECRYPTED FLAG: {flag}\n")
        
        return flag
    
    except UnicodeDecodeError:
        print("Could not decode as UTF-8, trying as raw bytes:")
        print(f"Raw bytes: {decrypted_bytes}")
        print(f"Hex representation: {decrypted_bytes.hex()}")
        
        return decrypted_bytes

def main():
    '''
    PUBLIC KEYS - GIVEN TO US BY THE CHALLENGE
    '''
    n = 8732851030901103315546024107527412423460054120791582645327296072030149520595598830189737190136429774375847088648891282895380791041462467946364644597106651
    e = 65537 
    
    '''
    PRIMES (FACTORIZED FROM n)
    https://factordb.com/index.php?query=8732851030901103315546024107527412423460054120791582645327296072030149520595598830189737190136429774375847088648891282895380791041462467946364644597106651
    '''
    p = 89434994450522445031250973494975469910185057723838915257965779692637908486619
    q = 97644675717314693028299287382143581611499104251746026552841672042065803811329
    
    # SECRET TO DECRYPT
    secret = b'55d4e09b61c53557c2a265141206ba394a92648e290c0377ca58aec1b6811254125590ea3393563c485bad44cd5c80b85c219927a8bea340a4aa39dd7310afca'
    
    '''
    COMPUTED PRIVATE KEY:
    621481258039317421665725566283288089827390518628743174966911956298710916948548154545116063634044871221939056383449529403124981022151995735949983128412161
    '''
    print("\n" + "="*50)
    print("COMPUTING PRIVATE KEY:")
    print("="*50)
    
    d = compute_private_key(e, p, q)
    print(f"Private Key is: \n{d}\n")
    
    # Decryption process (reverse of encryption)
    print("\n" + "="*50)
    print("DECRYPTION PROCESS")
    print("="*50)
    
    result = decrypt_secret(secret, d, n)
    
    if result:
        print(f"\nSUCCESS! The decrypted message is: \n{result}")
    else:
        print("\nERROR: Decryption failed or returned an empty result")

if __name__ == "__main__":
    main()