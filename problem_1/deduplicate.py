import csv
import sys
import time


def deduplicate_dataset(input_filename: str, output_filename: str) -> None:
    unique_rows = set()

    # for space complexity optimization
    # (dataset is sorted in terms of player_id)
    last_player_id = None

    with open(input_filename, 'r', newline='') as input_file, \
            open(output_filename, 'w', newline='') as output_file:

        csv_reader = csv.reader(input_file)
        csv_writer = csv.writer(output_file)

        csv_writer.writerow(next(csv_reader))

        for row in csv_reader:
            if not last_player_id:
                last_player_id = row[0]

            if last_player_id != row[0]:
                unique_rows.clear()
                last_player_id = row[0]

            unique_identifiers = row[0], row[1], row[2], row[3]
            if unique_identifiers not in unique_rows:
                unique_rows.add(unique_identifiers)
                csv_writer.writerow(row)


if len(sys.argv) != 2:
    print("Usage: python deduplicate.py <output_filename>")
    sys.exit(-1)

print("Deduplication process started!")

start_time = time.time()

output_filename = sys.argv[1]
if not output_filename.endswith('.csv'):
    output_filename += '.csv'

deduplicate_dataset("steam-200k.csv", output_filename)

end_time = time.time()

print("Done!")
print(f"Execution time: {end_time - start_time}")
