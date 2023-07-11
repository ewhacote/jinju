def minute(t):
  [h, m] = t.split(':')
  return int(h)*60 + int(m)

def solution(book_time):
  res = 0
  room = [0 for i in range(24*60 + 10)]
  for i in book_time:
    check_in = minute(i[0])
    check_out = minute(i[1]) + 10
    room[check_in] = += 1
    room[check_out] -= 1

  for i in range(1, len(room)):
    room[i] += room[i-1]
  res = max(room)
  return res
