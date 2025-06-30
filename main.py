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
    keywords = ['unstable', 'explosion', 'ERROR', 'FAIL','sysytem down']
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
    """
    파이썬 3.13 버전 설치
    """
    print('Hello Mars')
    """
    절대위치로 파일지정
    """
    log_file = r'C:\Users\52649\Documents\GitHub\python_codyseey\Step01\01\PYTHON-PBL01_01\mission_computer_main.log'
    problem_logs_file = r'C:\Users\52649\Documents\GitHub\python_codyseey\Step01\01\PYTHON-PBL01_01\mission_computer_main.log'
    read_log_file_reverse(log_file)
    extract_problem_logs(
        log_file,
        problem_logs_file
    )


if __name__ == '__main__':
    main()
