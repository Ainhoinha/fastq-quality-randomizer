# Script for Quality Modification in FASTQ Files

## Overview

This Python script is designed for modifying the quality values in FASTQ files, which are commonly used in bioinformatics for storing nucleotide sequences along with quality scores. It offers two modes of operation: forward and reverse, each applying different quality modification patterns to the input file.

## Development

During the development of this script, various Python libraries were utilized to ensure robust functionality:

- **Python**: Chosen for its versatility and extensive library support.
- **argparse**: Used for creating a robust command-line interface (CLI) that allows users to specify input files, output files, and operational modes (`-fw` for forward, `-rv` for reverse).
- **random**: Employed to generate randomized quality score patterns required for modifying the quality values in the FASTQ files.
- **os**: Facilitates file system operations such as checking file existence and managing file paths in a cross-platform manner.

## Features

### Modes

- **Forward Mode (`-fw`)**: Applies specific quality modification patterns tailored for forward sequences.
- **Reverse Mode (`-rv`)**: Applies different quality modification patterns suitable for reverse sequences.

### Command-line Arguments

The script uses argparse to handle command-line arguments:

- `-i` or `--input`: Specifies the input FASTQ file.
- `-o` or `--output`: Specifies the output FASTQ file.
- `-ow` or `--overwrite`: Allows overwriting the output file if it already exists.
- `-fw` or `--forward`: Activates forward mode for quality modification.
- `-rv` or `--reverse`: Activates reverse mode for quality modification.

### Usage

Example command to execute the script:

```
python script.py -i input.fastq -o output.fastq -fw  
```

### Implementation

The script verifies the file extensions, checks file existence, manages output file overwriting, and applies the appropriate quality modification functions based on the chosen mode.

### Quality Modification Functions

Functions are implemented to generate randomized quality score patterns for different segments of the FASTQ sequences, ensuring varied and realistic quality modifications.