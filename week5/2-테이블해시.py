def solution(data, col, row_begin, row_end):
    answer = 0
    data.sort(key=lambda x:(x[col-1],-x[0]))
    bit_val = 0
    for i in range(row_begin-1, row_end):
        val = 0
        for j in data[i]:
            val += (j % (i+1))
        bit_val = bit_val ^ val
    return bit_val
