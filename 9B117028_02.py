import json

# 讀取students.json
with open('C:\\Users\\ptg\\9B117028_02\\students.json', 'r', encoding='utf-8') as file:
    student_data = json.load(file)

# 以utf-8寫入students.json
with open('C:\\Users\\ptg\\9B117028_02\\students.json', 'w', encoding='utf-8') as file:
    json.dump(student_data, file, ensure_ascii=False, indent=4)

# 實現程式碼
def get_student_info(student_id):
    """
    根據學號返回該學生的個人資料字典。
    如果找不到該學生,則手動拋出 ValueError 與錯誤訊息供上層呼叫程式處理。
    """
    with open('students.json', 'r', encoding='utf-8') as file:
        students_data = json.load(file)

    for student in students_data:
        if student['student_id'] == student_id:
            return student
    raise ValueError(f"發生錯誤: 學號 {student_id} 找不到.")

def add_course(student_id, course_name, course_score):
    """
    為指定學生添加一門課程及其分數。
    如果找不到該學生,則手動拋出 ValueError 與錯誤訊息。
    使用斷言確保課程名稱與課程分數不可為空字串。
    """
    assert course_name and course_score, "課程名稱或分數不可空白."

    with open('students.json', 'r', encoding='utf-8') as file:
        students_data = json.load(file, ensure_ascii=False, indent=4)

    for student in students_data:
        if student['student_id'] == student_id:
            student['courses'].append({'name': course_name, 'score': course_score})
            with open('students.json', 'w', encoding='utf-8') as file:
                json.dump(students_data, file, indent=4)
            print("=>課程已成功新增。")
            return
    raise ValueError(f"發生錯誤: 學號 {student_id} 找不到.")

def calculate_average_score(student_data):
    """
    計算並返回該學生所有課程的平均分數。
    如果該學生沒有課程,則返回 0.0。
    """
    if 'courses' not in student_data or not student_data['courses']:
        return 0.0

    total_score = sum(course['score'] for course in student_data['courses'])
    return total_score / len(student_data['courses'])

if __name__ == '__main__':
    while True:
        print("*" * 50 + "選單" + "*" * 50)
        print("1. 查詢指定學號成績")
        print("2. 新增指定學號的課程名稱與分數")
        print("3. 顯示指定學號的各科平均分數")
        print("4. 離開")
        print("*" * 100)

        try:
            choice = int(input("請選擇操作項目："))
            if choice == 1:
                student_id = input("請輸入學號: ")
                student_info = get_student_info(student_id)
                print(f"=>學生資料: {json.dumps(student_info, ensure_ascii=False, indent=4)}")
            elif choice == 2:
                student_id = input("請輸入學號: ")
                course_name = input("請輸入要新增課程的名稱: ")
                course_score = float(input("請輸入要新增課程的分數: "))
                add_course(student_id, course_name, course_score)
            elif choice == 3:
                student_id = input("請輸入學號: ")
                student_info = get_student_info(student_id)
                average_score = calculate_average_score(student_info)
                print(f"=>各科平均分數: {average_score:.2f}")
            elif choice == 4:
                print("=>程式結束。")
                break
            else:
                print("=>請輸入有效的選項。")
        except ValueError as e:
            print(f"=>發生錯誤: {e}")
        except:
            print("=>其它例外: 課程名稱或分數不可空白.")