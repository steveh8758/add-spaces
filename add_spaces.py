# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 12:44:25 2024

@author: Steven, Hsin
@email: steveh8758@gmail.com
"""

import os
import sys
from re import sub

def is_chinese(char):
    """判斷一個 unicode 字元是否是漢字。"""
    return '\u4e00' <= char <= '\u9fa5'

def is_digit(char):
    """判斷一個 unicode 字元是否是十進制數字。"""
    return '\u0030' <= char <= '\u0039'

def is_alpha(char):
    """判斷一個 unicode 字元是否是字母。"""
    return '\u0041' <= char <= '\u005a' or '\u0061' <= char <= '\u007a'

def is_english_symbol(char):
    """判斷一個 unicode 字元是否是英文符號。"""
    english_symbols = [':', ';', '%', '!', '?', '`', '°', '*', '_', '<', '=', '>', '"', '$', '&', '\'', ',', '.', '~', '/', '@', '\\', '^', '|']
    return char in english_symbols

def is_english_left_bracket(char):
    """判斷一個 unicode 字元是否是英文左括號。"""
    return char in ['(', '[']

def is_english_right_bracket(char):
    """判斷一個 unicode 字元是否是英文右括號。"""
    return char in [')', ']']

def is_chinese_left_bracket(char):
    """判斷一個 unicode 字元是否是中文左括號。"""
    return char == '（'

def is_chinese_right_bracket(char):
    """判斷一個 unicode 字元是否是中文右括號。"""
    return char == '）'

def add_spaces(text, encoding):
    """在字串中添加合理的空格。"""
    new_text = ""
    need_special_processing = False
    char_list = list(text)
    length = len(char_list)

    for i in range(length):
        if i < length - 1:
            current_char = char_list[i]
            next_char = char_list[i + 1]

            # 中文與英文之間增加空格
            if (is_chinese(current_char) and is_alpha(next_char)) or (is_alpha(current_char) and is_chinese(next_char)):
                char_list[i] += " "
            # 英文與中文括號之間增加空格
            elif (is_alpha(current_char) and is_chinese_left_bracket(next_char)) or (is_chinese_right_bracket(current_char) and is_alpha(next_char)):
                char_list[i] += " "
            # 中文與英文括號之間增加空格
            elif (is_chinese(current_char) and is_english_left_bracket(next_char)) or (is_english_right_bracket(current_char) and is_chinese(next_char)):
                char_list[i] += " "
            # 中文與英文符號之間增加空格
            elif (is_chinese(current_char) and is_english_symbol(next_char)) or (is_english_symbol(current_char) and is_chinese(next_char)):
                char_list[i] += " "
                need_special_processing = True
            # 中文與數字之間增加空格
            elif (is_chinese(current_char) and is_digit(next_char)) or (is_digit(current_char) and is_chinese(next_char)):
                char_list[i] += " "
            # 數字與中文括號之間增加空格
            elif (is_digit(current_char) and is_chinese_left_bracket(next_char)) or (is_chinese_right_bracket(current_char) and is_digit(next_char)):
                char_list[i] += " "

        new_text += char_list[i]

    if need_special_processing:
        # 處理中文裡的粗體字和斜體字
        new_text = sub(r' \* ', '*', new_text)
        new_text = sub(r' \*\* ', '**', new_text)
        new_text = sub(r' _ ', '_', new_text)
        new_text = sub(r' __ ', '__', new_text)

    return add_space_between_digit_and_unit(new_text)

def add_space_between_digit_and_unit(text):
    """在數字與單位之間增加空格。"""
    units = ['bps', 'Kbps', 'Mbps', 'Gbps', 'B', 'KB', 'MB', 'GB', 'TB', 'PB', 'g', 'Kg', 't', 'h', 'm', 's']
    for unit in units:
        pattern = r'(?<=\d)' + unit  # Regex pattern
        replacement = ' ' + unit
        text = sub(pattern, replacement, text)
    return text

def process_file(file_name, encoding="utf-8"):
    """給文本文件的內容添加合理的空格，並生成處理過的新文件。"""
    dir_name = os.path.dirname(file_name)
    base_name = os.path.basename(file_name)
    new_file_name = os.path.join(dir_name, encoding + "-" + base_name) if dir_name else encoding + "-" + base_name

    try:
        with open(file_name, encoding=encoding) as file:
            lines = [add_spaces(line, encoding) for line in file]
    except (UnicodeDecodeError, IOError) as err:
        return str(err)

    try:
        with open(new_file_name, "w", encoding=encoding) as new_file:
            new_file.writelines(lines)
            print(f'完成添加空格，生成新文件: {new_file_name}')
            return '成功'
    except IOError as err:
        return str(err)

if __name__ == '__main__':
    args_count = len(sys.argv)
    supported_encodings = ['gb2312', 'gbk', 'utf-8', 'gb18030', 'hz', 'iso2022_jp_2', 'big5', 'big5hkscs']

    if args_count == 1:
        print('用法: python add_spaces.py /path/to/file 編碼(如 gbk, utf-8)')
        print('    或 python add_spaces.py /path/to/file')
    elif args_count == 2:
        for encoding in supported_encodings:
            if process_file(sys.argv[1], encoding) == '成功':
                print('處理完成')
                break
    elif args_count == 3:
        if sys.argv[2] in supported_encodings:
            print(process_file(sys.argv[1], sys.argv[2]))
        else:
            print(f'編碼 ({sys.argv[2]}) 錯誤！')
            print('支持的編碼為 ' + ', '.join(supported_encodings))
    else:
        print('用法: python add_spaces.py /path/to/file 編碼')
