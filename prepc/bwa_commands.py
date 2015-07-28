# ### Functions for mapping paired end reads to reference fasta using bwa-mem
# * bwa_index_ref - indexing reference genome
# * bwa_map_fq - maps paired reads using bwa mem algorithm


import sys
import time
import subprocess
import os

def bwa_index_ref(in_ref, log_dir):
    ''' Indexing reference sequence using bwa'''
    print "Indexing reference sequence with BWA"

    assert log_dir
    assert in_ref
    assert os.path.isfile(in_ref)
    assert os.path.isdir(log_dir)

    ## log files for standard out and error
    log_file = open(log_dir + "/bwa_index_ref"+ time.strftime("-%Y-%m-%d-%H-%M-%S.log"),'w')
    stderr_file = open(log_dir + "/bwa_index_ref"+ time.strftime("-%Y-%m-%d-%H-%M-%S.stder"),'w')

    ## run command
    bwa_index_command = ["bwa","index",in_ref]
    subprocess.call(bwa_index_command, stdout=log_file, stderr=stderr_file)

    assert os.path.isfile(log_file)
    assert os.path.isfile(stderr_file)

    log_file.close(); stderr_file.close()

def bwa_map_fq(in_ref, in_fq1, in_fq2, out_sam, log_dir):
    ''' Mapping paired-end reads to reference'''
    print "Mapping paired-end reads to reference"
    
    assert log_dir
    assert in_ref
    assert in_fq1
    assert in_fq2
    assert os.path.isfile(in_ref)
    assert os.path.isdir(log_dir)

    ## log files for standard out and error
    sam_file = open(out_sam,'w')
    stderr_file = open(log_dir + "/bwa_mem"+ time.strftime("-%Y-%m-%d-%H-%M-%S.stder"),'w')
    
    ## run command
    bwa_mem_command = ["bwa","mem","-t","8", in_ref,in_fq1]
    if in_fq2 != None:
        bwa_mem_command.append(in_fq2)
    subprocess.call(bwa_mem_command, stdout=sam_file, stderr=stderr_file)  

    assert os.path.isfile(sam_file)
    assert os.path.isfile(stderr_file)

    sam_file.close(); stderr_file.close()

def bwa_map_pacbio(in_ref, in_fq1, in_fq2, out_sam, log_dir):
    ''' Mapping paired-end reads to reference'''
    print "Mapping paired-end reads to reference"
    
    assert log_dir
    assert in_ref
    assert in_fq1
    assert os.path.isfile(in_ref)
    assert os.path.isdir(log_dir)

    ## log files for standard out and error
    sam_file = open(out_sam,'w')
    stderr_file_name = log_dir + "/bwa_mem"+ time.strftime("-%Y-%m-%d-%H-%M-%S.stder")
    stderr_file = open(stderr_file_name,'w')
    
    ## run command
    bwa_mem_command = ["bwa","mem","-x", "pacbio", "-t","8", in_ref,in_fq1]
    subprocess.call(bwa_mem_command, stdout=sam_file, stderr=stderr_file)  

    assert os.path.isfile(out_sam)
    assert os.path.isfile(stderr_file)

    sam_file.close(); stderr_file.close()