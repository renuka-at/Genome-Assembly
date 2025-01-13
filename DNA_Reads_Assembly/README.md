# DNA Read Assembly Script

## Overview:
This Python script is designed to assemble DNA sequencing reads from an input file in `.txt` format into contigs in `.fasta` format. It takes two command-line arguments: the input file path containing raw reads and the output file path to save the contigs.

## Features:
- Reads a list of DNA sequencing reads from a `.txt` file.
- Assembles the reads into longer contigs based on overlapping sequences using a greedy approach.
- Outputs the assembled contigs in a `.fasta` formatted file.
- Implements the `findOverlap()` function to check for overlaps and merge reads into contigs.

## Dependencies:
- Python 3.x
- Basic knowledge of Python and bioinformatics.

## File Structure:
1. **assembleReads.py**: The main script that assembles reads into contigs.
2. **Input file**: A `.txt` file containing DNA sequencing reads (one read per line).
3. **Output file**: A `.fasta` file where the assembled contigs are written.

## How It Works:

### Functions in the script:
- **`readReads(in_file)`**: Reads the input file line by line, storing each read as a list of strings.
- **`writeContigs(reads, out_file)`**: Takes a list of DNA sequencing reads and assembles them into contigs. The resulting contigs are written to the output file in the FASTA format.
- **`findOverlap(a, b, k)`**: Identifies an overlap of `k` bases between two sequences, either from the end of sequence `a` to the beginning of sequence `b`, or vice versa.

### Workflow:
1. **Input**: The script expects the following inputs:
   - A `.txt` file containing sequencing reads where each line is a DNA read.
   - The file path for the output `.fasta` file.
   
2. **Step 1**: `readReads(in_file)` reads the sequencing reads from the given input file and returns them as a list.
   
3. **Step 2**: In `writeContigs()`, the script iterates over the reads and merges overlapping sequences by using the `findOverlap()` function. It combines overlapping reads into contigs.
   
4. **Step 3**: The resulting contigs are written to an output `.fasta` file.

5. **Output**: The script outputs the contigs in the FASTA format, with each contig listed as `>Contig_n` followed by the sequence.

## Usage:
1. Place the script (`assembleReads.py`) in your working directory.
2. Prepare your input file containing raw sequencing reads in `.txt` format, with one sequence per line.
3. Run the script via the command line:
   
   ```python
   python3 assembleReads.py input_file.txt output_file.fasta
   ```

Replace input_file.txt with the path to your input file and output_file.fasta with the desired output file path.

Output Format:
The contigs will be written in FASTA format:
```python
>Contig_1
AGCTGAGCTAGCTAGCTAGC...
>Contig_2
GCTAGCTGAGCTAGGTCAG...
```
**Notes:**
The script uses a greedy approach to assemble the reads by iteratively finding overlaps between pairs of reads and merging them into longer sequences (contigs).
The findOverlap function looks for an overlap of at least k bases between the end of one read and the start of the next read (or vice versa).

**Limitations:**
The script does not handle mismatched or complex sequencing errors.
This is a basic approach for educational purposes and may not scale well with large datasets in real-life bioinformatics workflows.

Author:Renuka Athinarayanan
Developed for Northeastern University assignment
