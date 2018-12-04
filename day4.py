import re
from collections import defaultdict, Counter
import statistics


with open('day4-input.txt', 'r') as input_file:
    entries = sorted([entry.strip() for entry in input_file])

guards_minutes_slept = defaultdict(list)

TIMESTAMP_PATTERN = re.compile(r'^\[(?P<date>.+) (?P<time>.+)\]')
ID_PATTERN = re.compile(r'Guard #(\d+) begins shift$')
current_guard = ''
slept_at = ''

for entry in entries:
    # Sample entry
    # [1518-07-12 23:58] Guard #3449 begins shift
    date, time = re.match(TIMESTAMP_PATTERN, entry).groups()
    hour, minute = [int(x) for x in time.split(':')]
    id_match = re.search(ID_PATTERN, entry)

    # New shift starts
    if id_match:
        current_guard = int(id_match.group(1))
    elif 'falls asleep' in entry:
        slept_at = minute
    elif 'wakes up' in entry:
        # Get every minute since fell asleep
        guards_minutes_slept[current_guard].extend(range(slept_at, minute))


# guard_id: (minutes_slept, most_common_minute)
sleep_total = {}
# guard_id: (minute, times slept at this minute)
sleep_by_minute = {}

for guard_id, minutes_slept in guards_minutes_slept.items():
    try:
        mode = statistics.mode(minutes_slept)
    except statistics.StatisticsError:
        mode = None
    total_minutes_slept = len(minutes_slept)
    sleep_total[guard_id] = (total_minutes_slept, mode)
    sleep_by_minute[guard_id] = Counter(minutes_slept).most_common()[0]

longest_sleeper_id = max(sleep_total, key=lambda k: sleep_total[k][0])
longest_sleeper_minute = sleep_total[longest_sleeper_id][1]

# pt 1
print(longest_sleeper_id * longest_sleeper_minute)

consistent_sleeper_id = max(sleep_by_minute, key=lambda k: sleep_by_minute[k][1])
consistent_sleeper_minute = sleep_by_minute[consistent_sleeper_id][0]

# pt 2
print(consistent_sleeper_id * consistent_sleeper_minute)
