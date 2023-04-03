from .common.common import read_file_to_lines


class SimpleVM:
    def __init__(self, initial_val: int = 1) -> None:
        self.history = [initial_val]
        self.register = initial_val
        return

    def _pass_cycle(self) -> None:
        self.history.append(self.register)
        return

    def _update_register(self, value: int) -> None:
        self.register = value
        self._pass_cycle()
        return

    def run_command(self, command: str) -> None:
        if command == "noop":
            self._pass_cycle()
            return

        _, operand = command.split()
        value_to_add = int(operand)
        self._pass_cycle()
        self._update_register(self.register + value_to_add)
        return

    def get_pixel(self, cycle: int) -> str:
        sprit_middle_loc = self.history[cycle]
        x_loc_currently_painting = cycle % 40

        if abs(x_loc_currently_painting - sprit_middle_loc) < 2:
            return "#"
        return "."


def part1() -> int:
    lines = read_file_to_lines(__file__)

    vm = SimpleVM()
    for line in lines:
        vm.run_command(line.strip())

    interesting_indexes = [19, 59, 99, 139, 179, 219]
    register_snapshots = [vm.history[i] * (i + 1) for i in interesting_indexes]
    return sum(register_snapshots)


def part2() -> None:
    lines = read_file_to_lines(__file__)

    vm = SimpleVM()
    for line in lines:
        vm.run_command(line.strip())

    for i in range(6):
        cycle_window = range(i * 40, ((i + 1) * 40) + 1)
        chars = [vm.get_pixel(cycle) for cycle in cycle_window]
        print("".join(chars))
    return
