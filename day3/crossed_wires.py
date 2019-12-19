################################################################################
# Filename:
# crossed_wires.py
#
# Prerequisites:
# * Python3
#
# CLI usage:
# $ cd day3/
# $ python3 crossed_wires.py
#
# Python REPL usage:
# >>> from crossed_wires import FuelManagementSystem
# >>> wire1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"
# >>> wire2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"
# >>> fms = FuelManagementSystem(wire1, wire2)
# >>> fms.manhattan_dist_intersection_min()
# 135
# >>> fms.steps_combined_min()
# 410
# >>>
################################################################################

import re
from typing import List, Tuple

import numpy as np
from nptyping import Array


class FuelManagementSystem:
    def __init__(self, wire1: str, wire2: str):
        self.wire1 = wire1
        self.wire2 = wire2

    def steps_combined_min(self) -> int:
        trace_dir1 = self._trace_dir(self.wire1)
        trace_dir2 = self._trace_dir(self.wire2)
        mat_boundaries1 = self._mat_boundaries(trace_dir1)
        mat_boundaries2 = self._mat_boundaries(trace_dir2)
        origin_offset = self._origin_offset(mat_boundaries1, mat_boundaries2)
        trace_coord1 = self._trace_coord(trace_dir1, origin_offset)
        trace_coord2 = self._trace_coord(trace_dir2, origin_offset)
        mat_shape = self._mat_shape(trace_coord1, trace_coord2)
        mat_trace1 = self._mat_trace(trace_coord1, mat_shape, origin_offset)
        mat_trace2 = self._mat_trace(trace_coord2, mat_shape, origin_offset)
        intersections = self._intersections(mat_trace1, mat_trace2)
        return self._steps_combined_min(intersections, trace_coord1, trace_coord2)

    def manhattan_dist_intersection_min(self) -> int:
        trace_dir1 = self._trace_dir(self.wire1)
        trace_dir2 = self._trace_dir(self.wire2)
        mat_boundaries1 = self._mat_boundaries(trace_dir1)
        mat_boundaries2 = self._mat_boundaries(trace_dir2)
        origin_offset = self._origin_offset(mat_boundaries1, mat_boundaries2)
        trace_coord1 = self._trace_coord(trace_dir1, origin_offset)
        trace_coord2 = self._trace_coord(trace_dir2, origin_offset)
        mat_shape = self._mat_shape(trace_coord1, trace_coord2)
        mat_trace1 = self._mat_trace(trace_coord1, mat_shape, origin_offset)
        mat_trace2 = self._mat_trace(trace_coord2, mat_shape, origin_offset)
        intersections = self._intersections(mat_trace1, mat_trace2)
        return self._manhattan_dist_intersection_min(intersections, origin_offset)

    @staticmethod
    def _steps_combined_min(
        intersections: Array[np.int64, ..., 2],
        trace_coord1: List[Tuple[int, int]],
        trace_coord2: List[Tuple[int, int]],
    ) -> int:
        intersections_trace1 = {}
        intersections_trace2 = {}
        for i, e in enumerate(trace_coord1):
            if e in intersections:
                intersections_trace1[e] = i
        for i, e in enumerate(trace_coord2):
            if e in intersections:
                intersections_trace2[e] = i
        steps_combined_buffer = []
        for x_i, y_i in intersections:
            try:
                steps_combined_buffer.append(
                    intersections_trace1[(x_i, y_i)] + intersections_trace2[(x_i, y_i)]
                )
            except:
                pass
        return min(steps_combined_buffer)

    @staticmethod
    def _manhattan_dist_intersection_min(
        intersections: Array[np.int64, ..., 2], origin_offset: Tuple[int, int]
    ) -> int:
        x_offset, y_offset = origin_offset[0], origin_offset[1]
        manhattan_distances = []
        for x_i, y_i in intersections:
            manhattan_distance = abs(x_offset - x_i) + abs(y_offset - y_i)
            manhattan_distances.append(manhattan_distance)
        return min(manhattan_distances)

    @staticmethod
    def _intersections(
        mat_trace1: Array[np.int64], mat_trace2: Array[np.int64]
    ) -> Array[np.int64, ..., 2]:
        nonzeros = np.nonzero(mat_trace1 * mat_trace2)
        return np.transpose(np.array([nonzeros[1], nonzeros[0]]))

    @staticmethod
    def _mat_trace(
        trace_coord: List[Tuple[int, int]],
        mat_shape: Tuple[int, int],
        origin_offset: Tuple[int, int],
    ) -> Array[np.int64]:
        mat_buffer = np.zeros(mat_shape)
        for x_i, y_i in trace_coord:
            mat_buffer[y_i][x_i] = 1
        x_offset, y_offset = origin_offset[0], origin_offset[1]
        mat_buffer[y_offset][x_offset] = 0
        return mat_buffer

    @staticmethod
    def _mat_shape(
        trace_coord1: List[Tuple[int, int]], trace_coord2: List[Tuple[int, int]]
    ):
        x_max = 0
        y_max = 0
        for x_i, y_i in trace_coord1 + trace_coord2:
            if x_i > x_max:
                x_max = x_i
            if y_i > y_max:
                y_max = y_i
        return y_max + 1, x_max + 1

    @staticmethod
    def _trace_coord(
        trace_dir: List[Tuple[str, int]], origin_offset: Tuple[int, int]
    ) -> List[Tuple[int, int]]:
        x_0, y_0 = origin_offset[0], origin_offset[1]
        trace_coord_buffer = [(x_0, y_0)]
        for dir, steps in trace_dir:
            delta_x, delta_y = 0, 0
            if dir == "L":
                delta_x = -steps
            elif dir == "U":
                delta_y = steps
            elif dir == "D":
                delta_y = -steps
            elif dir == "R":
                delta_x = steps

            if delta_x < 0:
                for x_i in range(x_0 - 1, x_0 + delta_x - 1, -1):
                    trace_coord_buffer.append((x_i, y_0))
            elif delta_y > 0:
                for y_i in range(y_0 + 1, y_0 + delta_y + 1, 1):
                    trace_coord_buffer.append((x_0, y_i))
            elif delta_y < 0:
                for y_i in range(y_0 - 1, y_0 + delta_y - 1, -1):
                    trace_coord_buffer.append((x_0, y_i))
            elif delta_x > 0:
                for x_i in range(x_0 + 1, x_0 + delta_x + 1, 1):
                    trace_coord_buffer.append((x_i, y_0))
            x_0, y_0 = trace_coord_buffer[-1]
        return trace_coord_buffer

    @staticmethod
    def _origin_offset(
        mat_boundaries1: Tuple[int, int, int, int],
        mat_boundaries2: Tuple[int, int, int, int],
    ) -> Tuple[int, int]:
        x_offset = max(abs(mat_boundaries1[0]), abs(mat_boundaries2[0]))
        y_offset = max(abs(mat_boundaries1[2]), abs(mat_boundaries2[2]))
        return x_offset, y_offset

    @staticmethod
    def _mat_boundaries(trace_dir: List[Tuple[str, int]]) -> Tuple[int, int, int, int]:
        left_bound = 0
        upper_bound = 0
        lower_bound = 0
        right_bound = 0
        x_head = 0
        y_head = 0
        for step in trace_dir:
            if step[0] == "L":
                x_head = x_head - step[1]
                if x_head < left_bound:
                    left_bound = x_head
            elif step[0] == "U":
                y_head = y_head + step[1]
                if y_head > upper_bound:
                    upper_bound = y_head
            elif step[0] == "D":
                y_head = y_head - step[1]
                if y_head < lower_bound:
                    lower_bound = y_head
            elif step[0] == "R":
                x_head = x_head + step[1]
                if x_head > right_bound:
                    right_bound = x_head
        return left_bound, upper_bound, lower_bound, right_bound

    @staticmethod
    def _trace_dir(wire: str) -> List[Tuple[str, int]]:
        regex = re.findall(r"(U|D|L|R)(\d+)", wire)
        return [(dir, int(count)) for dir, count in regex]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        wires = f.read().split("\n")[:2]
    wire1 = wires[0]
    wire2 = wires[1]

    fms = FuelManagementSystem(wire1, wire2)
    print(fms.manhattan_dist_intersection_min())
    print(fms.steps_combined_min())
