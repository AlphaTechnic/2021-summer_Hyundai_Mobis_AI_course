import time


def left_move(pos, _):
    return max(0, pos - 1)


def right_move(pos, deCoded):
    return min(len(deCoded), pos + 1)


def del_ch(pos, deCoded):
    if pos == 0: return

    pos -= 1; del deCoded[pos]
    return pos


def insert_ch(pos, deCoded, ch):
    deCoded = deCoded[:pos] + [ch] + deCoded[pos:]
    pos += 1
    return deCoded, pos


def decodeString(string):
    """
    Recover a string from a keylog string
    :param string(문자열):
    :return: 복원된 문자열 반환

    :자료구조
    deCoded[] - 복원된 문자열 리스트
    pos - 현재 커서의 위치(deCoded에서의 index)
    """
    deCoded = []
    pos = 0
    for ch in string:
        if ch.isalnum():
            deCoded, pos = insert_ch(pos, deCoded, ch)
        else:  # action char : '<', '>', '-'
            pos = action_dic[ch](pos, deCoded)

    return ''.join(deCoded)


if __name__ == "__main__":
    input_file = open("keylog_in.txt", "rt")
    output_file = open("keylog_ans.txt", "wt")
    action_dic = {'<': left_move, '>': right_move, '-': del_ch}


    print("복원 시작")
    start = time.time()
    for string in input_file.readlines():
        string = string.rstrip()
        string_recovered = decodeString(string)
        output_file.write(string_recovered + '\n')
    end = time.time()
    print("복원 완료")

    print("수행 시간 : %.10f sec" % (end - start))

    input_file.close()
    output_file.close()
