#Parameters of S box
S_Box = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]

#Parameters of P box
P_Box = [1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

#generate subkeys from masterkey
def gen_K_list(K):                    # input is bitwise

    Ks = []
    for i in range(5, 0, -1):         # [k1,k2,k3,k4,k5]
        ki = K % (2 ** 16)
        Ks.insert(0, ki)
        K = K >> 4
    return Ks                         # output is a list with five element


def pi_s(s_box, ur):                  # inputs are list of s_box and int

    vr = 0                                        #applying s_box on input of s_box
    for i in range(4):
        uri = ur % (2 ** 4)
        vri = s_box[uri]
        vr = vr + (vri << (4 * i))
        ur = ur >> 4
    return vr                                     # output of s_box


def pi_p(p_box, vr):                              # inputs are list of p_box and int

    wr = 0                                        # applying p_box
    for i in range(15, -1, -1):
        vri = vr % 2
        vr = vr >> 1
        wr = wr + (vri << (16 - p_box[i]))
    return wr                                     # output of p_box


def do_SPN(x, s_box, p_box, Ks):                  # inputs are list and int

    wr = x
    for r in range(3):
        ur = wr ^ Ks[r]                         # XOR operation
        vr = pi_s(s_box, ur)                    # packet substitution
        wr = pi_p(p_box, vr)                    # single bit permutation

    ur = wr ^ Ks[3]
    vr = pi_s(s_box, ur)
    y = vr ^ Ks[4]
    return y                                    # output of spn


def encrypt(K, x):                            # encryption with key and plaintext

    Ks = gen_K_list(K)                        # generate subkeys
    return do_SPN(x, S_Box, P_Box, Ks)        # output of encryption
