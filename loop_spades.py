import os

# List all files ending with 'R1.fastq.gz' in the current directory
files_R1 = [f for f in os.listdir() if f.endswith('R1.fastq.gz')]

# List all files ending with 'R2.fastq.gz' in the current directory
files_R2 = [f for f in os.listdir() if f.endswith('R2.fastq.gz')]

# Iterate over pairs of corresponding R1 and R2 files
for file_R1, file_R2 in zip(files_R1, files_R2):
    # Generate output name by removing '_R1.fastq.gz' from the R1 file name
    output_name = file_R1.replace('_R1.fastq.gz', '')

    # Construct the SPAdes command
    command = f'spades.py -1 {file_R1} -2 {file_R2} --careful --cov-cutoff auto -o {output_name}'

    # Execute the SPAdes command using os.system
    os.system(command)
