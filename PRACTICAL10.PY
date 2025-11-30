import numpy as np
# simple helper: convert text to numbers and back (A=0..Z=25)
def text_to_nums(s):
    s = ''.join(ch for ch in s.upper() if ch.isalpha())
    return [ord(ch)-65 for ch in s]

def nums_to_text(nums):
    return ''.join(chr((n % 26)+65) for n in nums)

# message and 2x2 key (must be invertible mod26)
msg = "Linear Algebra is fun"
nums = text_to_nums(msg)
# pad to even length for 2x2 block
if len(nums) % 2:
    nums.append(23)   # pad with X

K = np.array([[3, 3],
              [2, 5]])   # determinant 3*5 - 3*2 = 9 => gcd(9,26)=1 invertible
print("Key K:\n", K)

# encode in blocks
encoded = []
for i in range(0, len(nums), 2):
    block = np.array(nums[i:i+2])
    cipher_block = (K.dot(block) % 26)
    encoded.extend(cipher_block.tolist())

ciphertext = nums_to_text(encoded)
print("Ciphertext:", ciphertext)

# decode: need inverse of K mod 26
det = int(round(np.linalg.det(K)))
# modular inverse of determinant mod 26
def egcd(a,b):
    if b==0: return (1,0,a)
    x,y,g = egcd(b, a%b)
    return (y, x - (a//b)*y, g)
inv_det = None
_, inv_det_candidate, g = egcd(det, 26)
if g==1:
    inv_det = inv_det_candidate % 26
# compute adjoint/inverse mod26
adj = np.array([[K[1,1], -K[0,1]], [-K[1,0], K[0,0]]])
K_inv_mod26 = (inv_det * adj) % 26
# decode blocks
decoded = []
for i in range(0, len(encoded), 2):
    block = np.array(encoded[i:i+2])
    plain_block = (K_inv_mod26.dot(block) % 26)
    decoded.extend(plain_block.tolist())
decoded_text = nums_to_text(decoded)
print("Decoded text:", decoded_text)
