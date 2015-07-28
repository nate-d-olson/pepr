# ###Whole genome vcf files
import sys
import re
import subprocess
from prepc.samtools_commands import *
from prepc.vcflib_commands import *

def main(analysis_params):
    for i in analysis_params['plat']:
        # whole genome variant calls
        bam_list = [analysis_params[j]['markdup_file'] for j in analysis_params[i]['accessions']]
        samtools_mpileup(in_ref=analysis_params['ref'],
                         in_bams=bam_list,
                         out_vcf=analysis_params[i]['consensus_vcf'],
                         log_dir=analysis_params[i]['consensus_base_log'])
        vcflib_vcf2tsv(in_vcf= analysis_params[i]['consensus_vcf'],
        			   out_tsv= analysis_params[i]['consensus_tsv'],
        			   log_dir=analysis_params[i]['consensus_base_log'])
