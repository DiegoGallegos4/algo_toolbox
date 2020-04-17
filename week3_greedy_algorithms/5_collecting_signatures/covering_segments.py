# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments):
    points = []
    sorted_segments = sorted(segments, key=lambda s: s[1])
    candidate = sorted_segments[0].end
    points.append(candidate)
    for s in sorted_segments:
        if not s.start <= candidate <= s.end:
            candidate = s.end
            points.append(candidate)
    return points


if __name__ == "__main__":
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    print(*points)
