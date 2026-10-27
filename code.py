INF = float("inf")

def to_minutes(t):
    h, m = map(int, t.split(":"))
    return 60 * h + m

def contains(s, e, t):
    if s <= e:
        return s <= t <= e
    else:
        return t >= s or t <= e

def lecture_interval(s, e, q):
    if contains(s, e, q[0]):
        return None

    indices = [i for i, t in enumerate(q) if contains(s, e, t)]
    
    if not indices:
        return INF

    return min(indices), max(indices)

def preprocess_cut(times, lectures, cut_index):
    q = times[cut_index:] + times[:cut_index]

    forbidden = set()
    for s, e in lectures:
        if contains(s, e, q[0]):
            for i in range(1, len(q)):
                if contains(s, e, q[i]):
                    forbidden.add(i)

    intervals = []
    for s, e in lectures:
        interval = lecture_interval(s, e, q)
        
        if interval is None:
            continue
        if interval == INF:
            return None

        l, r = interval
        
        if all(i in forbidden for i in range(l, r + 1)):
            return None

        intervals.append((l, r))

    return q, intervals, forbidden

def is_valid(m, intervals):
    valid = [[0,c] for c in range(1, m+1)]

    for l, r in intervals:
        for c in range(1, r+1):
            valid[c-1][1] = min(l, valid[c-1][1])
        for c in range(r+1, m+1):
            valid[c-1][0] = max(l, valid[c-1][0])
    return valid
    
def solve_line_dp(m, intervals, forbidden):
    min_right = min((r for _, r in intervals), default=m)

    OPT = [[INF] * (m + 1) for _ in range(m)]

    valid = is_valid(m, intervals)

    for b in range(1,m):
        if b not in forbidden and b <= min_right:
            OPT[0][b] = 1

    for c in range(1, m + 1):
        if c < m and c in forbidden:
            continue
            
        for b in range(1, c):
            if b < valid[c-1][0] or b >= valid[c-1][1]:
                continue
            
            min_prev = min(OPT[a][b] for a in range(b))
            if min_prev != INF:
                cost_increment = 0 if c == m else 1
                OPT[b][c] = min_prev + cost_increment

    answer = min(OPT[b][m] for b in range(m))

    return answer

def min_visits(times_input, lectures_input):
    times = sorted(set(to_minutes(t) for t in times_input))
    lectures = [(to_minutes(s), to_minutes(e)) for s, e in lectures_input]

    if not lectures:
        return 0

    m = len(times)
    if m == 0:
        return INF

    answer = INF
    
    for cut_index in range(m):
        result = preprocess_cut(times, lectures, cut_index)
        if result is None:
            continue
            
        q, intervals, forbidden = result

        if not intervals:
            answer = min(answer, 1)
            continue

        dp_answer = solve_line_dp(m, intervals, forbidden)
        
        if dp_answer != INF:
            answer = min(answer, 1 + dp_answer)

    return answer

if __name__ == "__main__":
    n = int(input("Enter number of available visit times: "))
    times_input = []

    print("Enter visit times in HH:MM format:")
    for _ in range(n):
        times_input.append(input().strip())

    k = int(input("Enter number of lectures: "))
    lectures_input = []

    print("Enter lecture start and end times (HH:MM HH:MM):")
    for _ in range(k):
        s, e = input().split()
        lectures_input.append((s, e))

    result = min_visits(times_input, lectures_input)

    if result == INF:
        print("Not possible to check every lecture exactly once.")
    else:
        print(f"Minimum visits required: {result}")
