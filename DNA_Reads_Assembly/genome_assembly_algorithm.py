import sys


def assembleReads(inp, outp_):
    """
    Takes in an input file containing reads in .txt format and returns an output file containing contigs in .fasta format

    """

    def readReads(in_file):
        """
        Takes in reads from a text file and coverts it into a list of reads
        """
        with open(in_file, "r") as i_file:
            reads = [line.strip() for line in i_file]
        return reads

    def writeContigs(reads, out_file):
        """
        Takes the list of reads and assembles into contigs and writes contigs to the specified output file
        """
        cont_list1 = []
        # iterate until the list is empty
        while len(reads) != 0:
            i = 0
            # Merges reads after overlap and removes the read after merging
            while i < len(reads)-1:
                first = reads[0]
                second = reads[i+1]

                # Calling the findOverlap function, to check for an overlap
                cont_s = findOverlap(first, second, k=10)

                if cont_s:
                    reads[0] = cont_s   # Extend the first read with the overlapping part of the second read

                    reads.pop(i+1)   # Remove the second read from the list
                    i = 0  # Reset to the beginning of the list to recheck for overlaps
                else:
                    i += 1  # Move to the next pair of reads

            cont_list1.append(reads[0])   # Add the extended read to the list
            reads.pop(0)    # remove that read from the original list

        # Remove reads that are part of contigs (in between portions) from the original list
            remove_read = []
            for read in reads:
                for cont in cont_list1:
                    if read in cont:
                        remove_read.append(read)
            reads[:] = [s for s in reads if s not in remove_read]

        # writing contigs to the output file
        with open(out_file, "w") as o_file:
            for index, element in enumerate(cont_list1):
                o_file.write(f'>Contig_{index+1}\n{element}\n')
        return cont_list1

    def findOverlap(a, b, k):
        """
        Finds and returns the overlap between two sequences a and b with a known overlap distance of k.
        """

        max_overlap = k
        cont = ""
        for overlap in range(1, min(len(a), len(b))+1):
            # overlap a to b
            f1 = a[-overlap:]
            f2 = b[:overlap]

            if f1 == f2:
                cont_12 = a[:-overlap] + b

                if overlap >= max_overlap:
                    cont = cont_12

            # overlap b to a
            r1 = b[-overlap:]
            r2 = a[:overlap]

            if r1 == r2:
                cont_21 = b[:-overlap] + a

                if overlap >= max_overlap:
                    cont = cont_21
        return cont

    # Read input sequences from the provided input file
    inp_reads = readReads(input_file)
    writeContigs(inp_reads, output_file)


# Get input and output file paths from command-line " python3 [file name] [input path] [output path]
input_file = sys.argv[1]
output_file = sys.argv[2]

assembleReads(input_file, output_file)





