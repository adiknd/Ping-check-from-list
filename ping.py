import subprocess

def check_ping(file_path):
    print("In progress ... ")
    with open(file_path, 'r') as ips_read:
        buff = ips_read.readlines()
    file_path_output = get_filepath_output(file_path)+'ips_result.txt'
    with open(file_path_output, 'w') as ips_write:
        for line in buff:
            line = str(line).strip()
            response = subprocess.call(('ping -n 1 -w 10 ' + line), stdout=subprocess.PIPE)
            if response == 0:
                ips_write.write(line+';YES\n')
            else:
                ips_write.write(line+';NO\n')
    print('Done.')
    print('Saved as: '+file_path_output)

def get_filepath_output(file_path):
    i = 1
    while True:
        if file_path[-i] == '\\':
            file_path_output = file_path[:-i + 1]
            break
        else:
            i += 1
    return file_path_output

if __name__ == '__main__':
    file_path = input("Enter path to file with IP addresses: ")
    check_ping(file_path)