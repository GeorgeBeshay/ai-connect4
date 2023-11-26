import math

# state = 0b_000000000_001000000_010000000_011000000_100000000_101000000_110000000
# print(state)
#
# width = 7
# height = 6
#
# for col in [0, 1, 2, 3, 4, 5, 6]:
#     mirrored_col = width - 1 - col     # 0 => 3 ,, 1 => 2 etc..
#     h_i_bits_count = math.ceil(math.log2(height + 1))
#     h_i_bits = (1 << h_i_bits_count) - 1
#     shift_len = height + (mirrored_col * (h_i_bits_count + height))
#     h_i = ((h_i_bits << shift_len) & state) >> shift_len
#     print(h_i)

