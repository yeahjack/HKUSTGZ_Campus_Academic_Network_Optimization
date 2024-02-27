import argparse

def process_file(file_path):
    channel = "🎯 全球直连"
    output_lines = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("*."):
                url_new = line[2:]
                suffix = "DOMAIN-SUFFIX"
            else:
                url_new = line
                suffix = "DOMAIN"
            
            output_line = f"  - {suffix},{url_new},{channel}"
            output_lines.append(output_line)

    output_file_path = file_path.replace('.txt', '_processed.txt')
    with open(output_file_path, 'w') as output_file:
        for line in output_lines:
            output_file.write(line + "\n")

    print(f"Processed file saved to {output_file_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process a txt file with URL patterns.')
    parser.add_argument('file_path', type=str, help='Path to the txt file containing URLs')
    args = parser.parse_args()

    process_file(args.file_path)
