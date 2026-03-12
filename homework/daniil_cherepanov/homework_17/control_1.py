import os
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Log analyzer")
    parser.add_argument("path", help="Path to log file or folder")
    parser.add_argument("--text", required=True, help="Text to search")
    return parser.parse_args()


def get_files(path):
    if os.path.isfile(path):
        return [path]

    files = []
    for name in os.listdir(path):
        full_path = os.path.join(path, name)
        if os.path.isfile(full_path):
            files.append(full_path)
    return files


def analyze_file(file_path, search_text):
    found_count = 0  # счетчик найденных фрагментов

    with open(file_path, encoding="utf-8") as file:
        current_time = None
        current_line_number = None
        block_lines = []

        for line_number, line in enumerate(file, 1):
            if line[:4].isdigit():
                if block_lines:
                    found_count += process_block(
                        file_path,
                        current_time,
                        current_line_number,
                        block_lines,
                        search_text
                    )

                parts = line.split()
                current_time = parts[0] + " " + parts[1] if len(parts) >= 2 else parts[0]
                current_line_number = line_number
                block_lines = [line]
            else:
                block_lines.append(line)

        if block_lines:
            found_count += process_block(
                file_path,
                current_time,
                current_line_number,
                block_lines,
                search_text
            )

    return found_count


def process_block(file_path, time, line_number, lines, search_text):
    block = " ".join(lines)
    found_in_block = 0

    if search_text.lower() in block.lower():
        words = block.split()
        for i, word in enumerate(words):
            if search_text.lower() in word.lower():
                start = max(0, i - 5)
                end = i + 6
                fragment = " ".join(words[start:end])
                fragment = fragment.replace(word, f"\033[31m{word}\033[0m")

                print(f"\nFile: {file_path}")
                print(f"Time: {time}")
                print(f"Line: {line_number}")
                print(f"Fragment: {fragment}")
                print("-" * 60)

                found_in_block = 1
                break

    return found_in_block


def main():
    args = parse_args()
    files = get_files(args.path)

    total_files = len(files)
    total_found = 0

    for file in files:
        total_found += analyze_file(file, args.text)

    print(f"\nProcessed files: {total_files}")
    print(f"Fragments found: {total_found}")


if __name__ == "__main__":
    main()
