# main.py

def read_log_file_reverse(filename):
    """
    Reads the log file and prints it in reverse order.

    :param filename: str - The name of the log file.
    """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines.reverse()
            for line in lines:
                print(line.rstrip())
    except FileNotFoundError:
        print('Error: File not found.')
    except IOError:
        print('Error: Could not read the file.')


def extract_problem_logs(filename, output_filename):
    """
    Extracts problem-related log entries into a separate file.

    :param filename: str - Path to the original log file.
    :param output_filename: str - Path for the extracted problem log file.
    """
    keywords = ['unstable', 'explosion', 'ERROR', 'FAIL']
    try:
        with open(filename, 'r', encoding='utf-8') as infile:
            problem_lines = []
            for line in infile:
                for keyword in keywords:
                    if keyword.lower() in line.lower():
                        problem_lines.append(line)
                        break

        if problem_lines:
            with open(output_filename, 'w', encoding='utf-8') as outfile:
                for line in problem_lines:
                    outfile.write(line)
    except FileNotFoundError:
        print('Error: File not found.')
    except IOError:
        print('Error: Could not read or write the file.')


def main():
    read_log_file_reverse('mission_computer_main.log')
    extract_problem_logs(
        'mission_computer_main.log',
        'problem_logs.log'
    )


if __name__ == '__main__':
    main()
