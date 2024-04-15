import json
import os

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
        students_data = json.load(file)

    found = False
    for student in students_data:
        if
