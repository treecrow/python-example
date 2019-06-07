import random

# 生成指定长度的验证码


def generate_code(code_len=4):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    code = ''
    for _ in range(code_len):
        extract_index = random.randint(0, len(all_chars)-1)
        code += all_chars[extract_index]
    return code


print(generate_code())
print(generate_code(8))
