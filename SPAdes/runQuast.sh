#!/usr/bin/env bash
# runQuast.sh
function Quast {
    quast.py -o ../results ../results/rhodo/contigs.fasta 
}

Quast
