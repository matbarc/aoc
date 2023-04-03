from .common.common import read_file_to_string
from typing import Optional, Callable

test_input = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""


class Directory:
    def __init__(self, name: str, parent: Optional["Directory"] = None) -> None:
        self.name = name
        self.contents = []
        self.parent = parent
        return

    @property
    def size(self) -> int:
        return sum([file.size for file in self.contents])

    def __repr__(self) -> str:
        return f"/{self.name} ({self.size:,})"


class File:
    def __init__(self, name: str, size: int) -> None:
        self.name = name
        self.size = size
        return


ROOT_DIR = Directory("/")


def part1() -> int:
    file_str = read_file_to_string(__file__)
    blocks = [block.strip().splitlines() for block in file_str.split("$") if block]

    current_directory = None
    for block in blocks:
        cmd, *output = block
        current_directory = simulate_command(cmd, output, current_directory)

    return sum(
        [dir.size for dir in find_directories(ROOT_DIR, lambda d: d.size <= 100_000)]
    )


def part2() -> int:
    file_str = read_file_to_string(__file__)
    blocks = [block.strip().splitlines() for block in file_str.split("$") if block]

    current_directory = None
    for block in blocks:
        cmd, *output = block
        current_directory = simulate_command(cmd, output, current_directory)

    total_size = 70_000_000
    root_size = ROOT_DIR.size
    update_size = 30_000_000
    space_to_free = update_size - (total_size - root_size)

    matching_dirs = find_directories(ROOT_DIR, lambda d: d.size >= space_to_free)

    return min(matching_dirs, key=lambda x: x.size).size


def simulate_command(
    cmd: str, output: Optional[list[str]], current_directory: Optional["Directory"]
) -> Optional["Directory"]:
    if cmd == "cd /":
        current_directory = ROOT_DIR
    elif not current_directory:
        raise ValueError("Simulation needs to know cwd")
    elif cmd == "ls":
        if not output:
            raise ValueError("ls command needs output")
        contents = parse_ls_output(output, current_directory)
        current_directory.contents = contents
    elif cmd == "cd ..":
        current_directory = current_directory.parent
    elif cmd.startswith("cd "):
        dir_name = cmd[3:]
        for file in current_directory.contents:
            if type(file) == Directory and file.name == dir_name:
                current_directory = file
    return current_directory


def pretty_print(filelike, indent: int = 0) -> str:
    if type(filelike) == File:
        return f"{'  ' * indent}- {filelike.name} (file, size={filelike.size})"

    return "\n".join(
        [
            f"{'  ' * indent}- {filelike.name} (dir)",
            *[pretty_print(file, indent=indent + 1) for file in filelike.contents],
        ]
    )


def parse_ls_output(output: list[str], current_directory: Directory):
    files = []
    for line in output:
        if line.startswith("dir"):
            files.append(Directory(line[4:], current_directory))
            continue

        size_str, name = line.split()
        files.append(File(name, int(size_str)))
    return files


def find_directories(
    root: Directory, filter_fcn: Callable[[Directory], bool]
) -> list[Directory]:
    found = [root] if filter_fcn(root) else []
    for filelike in root.contents:
        if not isinstance(filelike, Directory):
            continue

        found.extend(find_directories(filelike, filter_fcn))
    return found
