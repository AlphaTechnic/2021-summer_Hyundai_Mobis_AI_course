D = {20111111: ['sam', 92, 85, 65], 20101234: ['joe', 100, 90, 75],
     20124321: ['Anne', 95, 90, 90], 20135555: ['Jane', 55, 60, 65]}


def add_data():
    try :
        st_id = int(input("학번을 입력하세요: "))
        if st_id in D:
            print("이미 입력된 학생입니다.")
            return
        name = input("이름을 입력하세요: ")
        ko = int(input("국어성적을 입력하세요: "))
        en = int(input("영어성적을 입력하세요: "))
        ma = int(input("수학성적을 입력하세요: "))
    except:
        print("잘못된 입력 입니다.")
        return

    D[st_id] = [name, ko, en, ma, (ko + en + ma) // 3]
    print("학생의 성적을 입력했습니다.")


def delete_data():
    try:
        st_id = int(input("삭제하기 원하는 학생의 학번을 입력하세요: "))
        if st_id not in D:
            print("없는 학생입니다.")
            return
        del D[st_id]
        print("학번: %s 학생의 정보를 삭제했습니다." % st_id)

    except:
        print("잘못된 입력입니다.")
        return


def print_data():
    print("학번        이름       국어  영어  수학   평균")
    print("------------------------------------------")
    for st_id, scores in D.items():
        print("%-8s   %-8s   %3s  %3s  %3s   %3s"
              % (st_id, scores[0], scores[1], scores[2], scores[3], scores[4]))


def exit_program():
    exit(0)


if __name__ == "__main__":
    for st_id, scores in D.items():
        mean = (scores[1] + scores[2] + scores[3]) // 3
        D[st_id].append(mean)
    print_data()

    err_flag = False
    print("------------------------------------------")
    print("1. 추가, 2. 삭제, 3. 출력, 4. 종료")
    try:
        N = int(input("숫자를 선택하세요: "))
        if N not in range(1, 5):
            raise Exception()
    except:
        err_flag = True
        print("잘못된 입력입니다.")

    if not err_flag:
        fun_dic = {1: add_data, 2: delete_data, 3: print_data, 4: exit_program}
        fun_dic[N]()

    while True:
        for st_id, scores in D.items():
            mean = (scores[1] + scores[2] + scores[3]) // 3
            D[st_id].append(mean)

        print("------------------------------------------")
        print("1. 추가, 2. 삭제, 3. 출력, 4. 종료")
        try:
            N = int(input("숫자를 선택하세요: "))
            if N not in range(1, 5):
                raise Exception()
        except:
            print("잘못된 입력입니다.")
        fun_dic = {1: add_data, 2: delete_data, 3: print_data, 4: exit_program}
        fun_dic[N]()
