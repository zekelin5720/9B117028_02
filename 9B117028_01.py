# 定義函式：取得偶數的平方值列表
def get_even_squares(num_list):
    # 使用列表推導式遍歷 num_list 中的每個數字，如果是偶數則計算其平方值並返回
    return [num ** 2 for num in num_list if num % 2 == 0]

# 定義函式：取得奇數的立方值列表
def get_odd_cubes(num_list):
    # 建立一個空列表，用於存儲奇數的立方值
    odd_cubes = []
    # 使用迴圈遍歷 num_list 中的每個數字
    for num in num_list:
        # 如果是奇數，則計算其立方值並加入到 odd_cubes 列表中
        if num % 2 != 0:
            odd_cubes.append(num ** 3)
    # 返回奇數立方值列表
    return odd_cubes

# 定義函式：取得從第 5 個元素開始到最後一個元素的子列表
def get_sliced_list(num_list):
    # 使用切片從第 5 個元素開始取到最後一個元素（包含最後一個元素），並返回子列表
    return num_list[4:]

# 定義函式：格式化數字列表，將每個數字格式化為 8 個字元的寬度，並靠右對齊
def format_numbers(numbers):
    # 建立一個空列表，用於存儲格式化後的數字
    formatted_numbers = []
    # 使用迴圈遍歷數字列表中的每個數字
    for num in numbers:
        # 將每個數字格式化為 8 個字元的寬度，並靠右對齊，然後加入到 formatted_numbers 列表中
        formatted_numbers.append(f"{num:8d}")
    # 返回格式化後的數字列表
    return formatted_numbers

if __name__ == "__main__":
    # 定義整數列表
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # 分別呼叫前 3 個函式，獲取偶數平方值列表、奇數立方值列表、切片子列表
    even_squares = get_even_squares(num_list)
    odd_cubes = get_odd_cubes(num_list)
    sliced_list = get_sliced_list(num_list)

    # 將獲取的結果進行數字格式化
    formatted_even_squares = format_numbers(even_squares)
    formatted_odd_cubes = format_numbers(odd_cubes)
    formatted_sliced_list = format_numbers(sliced_list)

    # 使用 print() 與 join() 輸出結果
    print(", ".join(formatted_even_squares))
    print(", ".join(formatted_odd_cubes))
    print(", ".join(formatted_sliced_list))