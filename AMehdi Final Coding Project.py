#Programmar Name: Abbas Mehdi
#Date: 12/8/23
#Program Description: Final Project, to read a file, find all the suspect IP addresses that might have been used by OUCH, and produce anoutput report to both the screen and to an output file.

def check_input_file():
    not_valid = True
    while not_valid:
        try:
            ip_file = input('Enter the input name: ')
            file_name = open(ip_file, 'r')
            not_valid = False
            return file_name
        except IOError:
            print('ERROR -- There is an issue with the file  ')


def main():
    file_address = check_input_file()
    suspect_ip_list = []
    suspect_date_time_list = []

    print('Output Report')

    # Read data from the file
    total_records = 0
    suspect_records = 0
    for line in file_address:
        total_records += 1
        ip_address = line[0:15]
        if is_suspect_ip(ip_address):
            suspect_records += 1
            date_and_time = line[16:47]  
            suspect_ip_list.append(ip_address)
            suspect_date_time_list.append(date_and_time)

    # Write the output
    output_file = input('Enter the output file name: ')
    output = open(output_file, 'w')
    output.write('Output Report\n')
    output.write('-------------\n')
    output.write(f'\nThe total number of records in the file is: {total_records}\n')
    output.write(f'\nThe number of suspect IP addresses is: {suspect_records}\n')
    output.write(f'\nThe percentage of suspect IP addresses is: {suspect_records / float(total_records) * 100:.3f}\n')
    output.write('\nSuspect IP Addresses\n')
    output.write('--------------------\n')

    # Compare and write the suspect IPs 
    for i in range(len(suspect_ip_list)):
        for j in range(i + 1, len(suspect_ip_list)):
            if suspect_ip_list[i] > suspect_ip_list[j]:
            # Swap the elements
                temp_ip = suspect_ip_list[i]
                suspect_ip_list[i] = suspect_ip_list[j]
                suspect_ip_list[j] = temp_ip

                temp_date_time = suspect_date_time_list[i]
                suspect_date_time_list[i] = suspect_date_time_list[j]
                suspect_date_time_list[j] = temp_date_time

    # Write the sorted IPs to the output file
    for i in range(len(suspect_ip_list)):
        output.write(f"IP Address = {suspect_ip_list[i]}  Date and Time = {suspect_date_time_list[i]}\n")

    output.write('Program complete!\n')
    output.close()

    print('Program complete!')

def is_suspect_ip(ip_line):
    # Extract the IP address from the input line
    ip_address = ip_line[:15]

    # Split the IP address into octets
    octets = ip_address.split('.')

    # Check if the first two octets are in the suspect range
    if len(octets) == 4 and 0 <= int(octets[0]) <= 255 and 0 <= int(octets[1]) <= 255:
        return f"{int(octets[0]):03d}.{int(octets[1]):03d}" in ['168.193', '224.174', '233.012']
    else:
        return False

main()
