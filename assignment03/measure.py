from math import gcd
from time import perf_counter_ns

def RSA(p: int, q: int, message: int):
    t_total_start = perf_counter_ns()

    t_keygen_start = perf_counter_ns()

    n = p * q

    t = (p - 1) * (q - 1)
    for i in range(2, t):
        if gcd(i, t) == 1:
            e = i
            break
    j = 0
    while True:
        if (j * e) % t == 1:
            d = j
            break
        j += 1
    t_keygen_end = perf_counter_ns()
    keygen_time = t_keygen_end - t_keygen_start
    # encryption
    t_enc_start = perf_counter_ns()
    ct = (message ** e) % n
    t_enc_end = perf_counter_ns()
    enc_time = t_enc_end - t_enc_start

    # decryption
    t_dec_start = perf_counter_ns()
    mes = (ct ** d) % n
    t_dec_end = perf_counter_ns()
    dec_time = t_dec_end - t_dec_start

    total_time = perf_counter_ns() - t_total_start

    # output
    print(f"Encrypted message is {ct}")
    print(f"Decrypted message is {mes}")

    print("--- Timing (nanoseconds) ---")
    print(f"Key generation time: {keygen_time}")
    print(f"Encryption time:     {enc_time}")
    print(f"Decryption time:     {dec_time}")
    print(f"Total runtime:       {total_time}")
    print("----------------------------\n")


# Testcase - 1
RSA(p=53, q=59, message=89)

# Testcase - 2
RSA(p=3, q=7, message=12)
