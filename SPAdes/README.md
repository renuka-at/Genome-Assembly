# Genome Assembly for *Rhodobacter spheroides*

**Author:** Renuka Athinarayanan  
**Date Created:** March 17th, 2023

## Overview:
This set of Bash scripts is designed to streamline the process of genome assembly for the organism *Rhodobacter spheroides*. The pipeline retrieves NGS reads, trims Illumina adapter sequences, assembles the genome using SPAdes, and evaluates the genome quality using QUAST. The scripts were tested on Northeastern University's Discovery cluster and utilize the `fasterq-dump` and `Trimmomatic` tools for preprocessing, and SPAdes and QUAST for assembly and quality control, respectively.

## Workflow Overview:
1. **getNGS.sh**: Retrieves NGS reads for *Rhodobacter spheroides* using the `fasterq-dump` tool. This step outputs FASTQ files containing raw sequencing data.
2. **trim.sh**: Processes the raw FASTQ files, trimming Illumina adapters and quality filtering using `Trimmomatic`. It outputs trimmed paired and unpaired FASTQ files.
3. **runSpades.sh**: Takes the trimmed reads and assembles them into contigs using the `SPAdes` genome assembler.
4. **runQuast.sh**: Runs the `QUAST` tool to evaluate the quality of the assembled genome by comparing it to the original reads.
5. **sbatch_assembleGenome.sh**: A SLURM batch script that automates the execution of all the above scripts, from downloading NGS reads to assembling the genome and analyzing it. This script is designed to run on the Discovery computing cluster at Northeastern University.

## Scripts and Their Functionality:

1. **getNGS.sh**  
   - Retrieves sequencing data using `fasterq-dump` from the specified SRR ID, which corresponds to the SRA dataset for *Rhodobacter spheroides*.

2. **trim.sh**  
   - Trims adapter sequences and filters low-quality sequences using the `Trimmomatic` tool.
   - Paired and unpaired trimmed reads are saved to the `../data/trimmed/` directory.

3. **runSpades.sh**  
   - Assembles trimmed paired-end FASTQ reads into contigs using the `spades.py` assembler.
   - Assembles reads from `../data/trimmed/paired/` into `../results/rhodo/`.

4. **runQuast.sh**  
   - Evaluates the quality of the genome assembly using the `QUAST` tool.
   - The output is stored in the `../results/quast_results/` folder, providing detailed metrics on the assembly.

5. **sbatch_assembleGenome.sh**  
   - Submits a batch job to the SLURM scheduler, running the entire pipeline in sequence, from data retrieval through genome assembly and evaluation.
   - Includes resource requests such as partition, job name, and time limits.

## Required Dependencies:
- **`fasterq-dump`**: A tool to download SRA dataset files as FASTQ.
- **`Trimmomatic`**: For trimming Illumina adapter sequences and filtering low-quality sequences.
- **`SPAdes`**: For assembling genomes from short-read data.
- **`QUAST`**: For analyzing the quality of genome assemblies.
- **SLURM**: For job scheduling and resource management on the Discovery cluster.
- **Anaconda3**: For environment management and tool installation.

## Workflow Execution:
1. **Step 1**: Execute the `sbatch_assembleGenome.sh` script to run the entire genome assembly pipeline.
2. **Step 2**: The pipeline will automatically download the NGS reads, trim the adapters, assemble the genome, and evaluate its quality.
3. **Step 3**: Once completed, the results will be stored in the `../results/rhodo/` (for assembly) and `../results/quast_results/` (for quality analysis) directories.

## Notes:
- Ensure that you are running these scripts on the computing cluster or an equivalent environment that has the necessary tools installed.
- Modify paths and parameters for local system configurations if needed.

## Author:
Renuka Athinarayanan  
Developed for Northeastern University BINF6308 course work.
