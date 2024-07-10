import argparse
import random
import os



### FORWARD
def generate_quality_first_bases_fw(read_length):
    return ''.join(random.choice('?@ABCD') for _ in range(int(read_length * 0.01)))

def generate_quality_next_bases_fw(read_length):
    return ''.join(random.choice('ABCDEG') for _ in range(int(read_length * 0.01)))

def generate_quality_middle_bases_fw(read_length):
    return ''.join(random.choice('FGH') for _ in range(int(read_length * 0.05)))

def generate_quality_last_bases_fw(read_length):
    return ''.join(random.choice('HI') for _ in range((int(read_length * 0.70))))

def generate_quality_decreasing_200_220_fw(read_length):
    return ''.join(random.choice('CDEFGH') for _ in range(int(read_length * 0.10)))

def generate_quality_decreasing_220_260_fw(read_length):
    return ''.join(random.choice('ABCDEG') for _ in range(int(read_length * 0.10)))

def generate_quality_decreasing_260_290_fw(read_length):
    return ''.join(random.choice('?@ABCD') for _ in range(int(read_length * 0.02)))

def generate_quality_decreasing_290_300_fw(read_length):
    return ''.join(random.choice('?@AB') for _ in range(int(read_length * 0.01)))

def change_quality_fw(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line_num, line in enumerate(f_in):
            if line_num % 4 == 0:
                f_out.write(line)
            elif line_num % 4 == 1:
                f_out.write(line)
            elif line_num % 4 == 2:
                f_out.write(line)
            else:
                read_length = len(line.strip())
                new_quality = (
                    generate_quality_first_bases_fw(read_length) +
                    generate_quality_next_bases_fw(read_length) +
                    generate_quality_middle_bases_fw(read_length) +
                    generate_quality_last_bases_fw(read_length) +
                    generate_quality_decreasing_200_220_fw(read_length) +
                    generate_quality_decreasing_220_260_fw(read_length) +
                    generate_quality_decreasing_260_290_fw(read_length) +
                    generate_quality_decreasing_290_300_fw(read_length)
                )
                f_out.write(new_quality + '\n')


### REVERSE
def generate_quality_first_bases_rv(read_length):
    return ''.join(random.choice('?@ABCD') for _ in range(int(read_length * 0.01)))

def generate_quality_next_bases_rv(read_length):
    return ''.join(random.choice('ABCDEG') for _ in range(int(read_length * 0.01)))

def generate_quality_middle_bases_rv(read_length):
    return ''.join(random.choice('EFGH') for _ in range(int(read_length * 0.02)))

def generate_quality_main_bases_rv(read_length):
    return ''.join(random.choice('HI') for _ in range((int(read_length * 0.10) * 6) + (int(read_length * 0.05))))

def generate_quality_decreasing_175_200_rv(read_length):
    return ''.join(random.choice('CDEFGH') for _ in range(int(read_length * 0.10)))

def generate_quality_decreasing_200_220_rv(read_length):
    return ''.join(random.choice('ABCDEG') for _ in range(int(read_length * 0.10)))

def generate_quality_decreasing_220_260_rv(read_length):
    return ''.join(random.choice('?@ABCD') for _ in range(int(read_length * 0.05)))

def generate_quality_decreasing_260_290_rv(read_length):
    return ''.join(random.choice('?@ABC') for _ in range(int(read_length * 0.04)))

def generate_quality_decreasing_290_300_rv(read_length):
    return ''.join(random.choice('?@AB') for _ in range(int(read_length * 0.02)))

def change_quality_rv(input_file, output_file):
    with open(input_file, 'r') as f_in, open(output_file, 'w') as f_out:
        for line_num, line in enumerate(f_in):
            if line_num % 4 == 0:
                f_out.write(line)
            elif line_num % 4 == 1:
                f_out.write(line)
            elif line_num % 4 == 2:
                f_out.write(line)
            else:
                read_length = len(line.strip())
                new_quality = (
                    generate_quality_first_bases_rv(read_length) +
                    generate_quality_next_bases_rv(read_length) +
                    generate_quality_middle_bases_rv(read_length) +
                    generate_quality_main_bases_rv(read_length) +
                    generate_quality_decreasing_175_200_rv(read_length) +
                    generate_quality_decreasing_200_220_rv(read_length) +
                    generate_quality_decreasing_220_260_rv(read_length) +
                    generate_quality_decreasing_260_290_rv(read_length) +
                    generate_quality_decreasing_290_300_rv(read_length)
                )
                f_out.write(new_quality + '\n')



### COMMANDS
# Create the parser
parser = argparse.ArgumentParser(description='Script to change the quality of a FASTQ file.')

# Mandatory commands
parser.add_argument('-i', '--input', type=str, required=True, help='Input ".fastq" file')
parser.add_argument('-o', '--output', type=str, required=True, help='Output file')
parser.add_argument('-ow', '--overwrite', action='store_true', help='Force overwrite output')

# Mutually exclusive group of arguments
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-fw', '--forward', action='store_true', help='Forward mode (default)')
group.add_argument('-rv', '--reverse', action='store_true', help='Reverse mode')

# Parse the arguments
args = parser.parse_args()


def main():
    # Check if input file is 'fastq'
    if not args.input.endswith('.fastq'):
        print("The input needs to be '.fastq'")
        return

    # Check if the input file not exists
    if not os.path.exists(args.input):
        print("The input file does not exists")
        return

    # Check if output file is 'fastq'
    if not args.output.endswith('.fastq'):
        print("The output needs to be '.fastq'")
        return

    # Check if the input and the output are the same
    if os.path.abspath(args.input) == os.path.abspath(args.output):
        base, ext = os.path.splitext(args.output)
        args.output = base + "_changed" + ext
        print("The input file are the same as output file.")
        print("Saving the output as: ", args.output)

    # Check if the output file exists
    if not args.overwrite and os.path.exists(args.output):
        print(args.output, "file already exists, use -ow to force the overwrite")
        return

    # Execute change quality
    if args.forward:
        change_quality_fw(args.input, args.output)
        print("Qualitys changed successfully (forward) and saved at:", args.output)
    elif args.reverse:
        change_quality_rv(args.input, args.output)
        print("Qualitys changed successfully (reverse) and saved at:", args.output)

if __name__ == "__main__":
    main()
