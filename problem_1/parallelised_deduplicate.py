import csv
import sys
import time
import multiprocessing


def func(lines):
    result = []
    unique_lines = set()

    for line in lines:
        unique_identifiers = line[0], line[1], line[2], line[3]
        if unique_identifiers not in unique_lines:
            unique_lines.add(unique_identifiers)
            result.append(line)

    return result


def deduplicate_dataset(input_filename: str, output_filename: str) -> None:
    with open(input_filename, 'r', newline='') as input_file, \
            open(output_filename, 'w', newline='') as output_file:
        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)
        last_player_id = None

        lines_matrix = []
        lines = []
        for row in csv_reader:
            if last_player_id != row[0]:
                if lines:
                    lines_matrix.append(lines)
                    lines = []
                last_player_id = row[0]
            lines.append(row)

        if lines:
            lines_matrix.append(lines)

        with multiprocessing.Pool() as pool:
            results = pool.map(func, lines_matrix)

            for result in results:
                for row in result:
                    csv_writer.writerow(row)



if __name__ == "__main__":
    output_filename = ""
    if len(sys.argv) != 2:
        output_filename = "parallelised_out.csv"
    else:
        output_filename = sys.argv[1]

    print("Deduplication process started!")

    start_time = time.time()

    if not output_filename.endswith('.csv'):
        output_filename += '.csv'

    deduplicate_dataset("steam-200k.csv", output_filename)

    end_time = time.time()

    print("Done!")
    print(f"Execution time: {end_time - start_time}")