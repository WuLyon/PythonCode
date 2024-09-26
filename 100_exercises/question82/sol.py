import zlib
ori_str = b'HelloworldHelloworldHelloworldHelloworldHelloworldHelloworldHelloworld'
print(f'ori_str = {ori_str}')

compress_str = zlib.compress(ori_str)
print(f'compress_str = {compress_str}')

decompress_str = zlib.decompress(compress_str)
print(f'decompress_str = {decompress_str}')
