from grades import *



students = {'Mike': 10,
            'Bob': 9,
            'Jane': 9,
            'Lisa': 7,
            'Kert': 8
            }

grades_lst = students.values()
if __name__ == "__main__":
    print(f"meen grade: {max_meen(grades_lst)}")
    print(f"max grade: {get_max(grades_lst)}")
    print(f"min grade: {get_min(grades_lst)}")



