## Pipeline for performing pairwise somatic variant calling
import sys
import re
import subprocess
from prepc.samtools_commands import *
from prepc.varscan_commands import *

def main(analysis_params):
    # nested for loops for pairwise comparisons
    for i in analysis_params['homogeneity']['pairs']:
        print i
        samtools_mpileup_pairs(in_ref= analysis_params['ref'], 
                               in_bams= [analysis_params[i]['bam1_file'], 
                                            analysis_params[i]['bam2_file']],
                               out_mpileup=analysis_params[i]['mpileup_file'], 
                               log_dir=analysis_params[i]['homogeneity_log'])
        varscan_somatic(in_mpileup=analysis_params[i]['mpileup_file'], 
                        snp_out=analysis_params[i]['varscan_snp_file'], 
                        indel_out=analysis_params[i]['varscan_indel_file'], 
                        log_dir=analysis_params[i]['homogeneity_log'])            



# if __name__ == '__main__':
#     main(sys.argv[1])

# Code from Justin used to characterize human RM
'''
echo "Running job $JOB_NAME, $JOB_ID on $HOSTNAME"
   path/samtools-0.1.18/samtools mpileup -q 1 -f /projects/justin.zook/from-projects/references/human_g1k_v37.fasta $BAM1 $BAM2 | java -jar -Xmx2g path/varscan/VarScan.v2.3.6.jar somatic - --output-snp "$OUTSTART"_snp.txt --output-indel "$OUTSTART"_indel.txt --mpileup 1 --min-coverage $COV  --min-coverage-tumor $COV --min-coverage-normal $COV --somatic-p-value 0.001

# hold off for now ....
#Filter output for sites with cov < 300 and change to csv for analysis in R
cat "$OUTSTART"_indel.txt | awk '$5 + $6 < 300' | awk '{ print $1,$2,$3,$4,$5,$6,$9,$10,$15 }' | sed 's/\ /,/g' > "$OUTSTART"_indel_covlt300.csv
cat "$OUTSTART"_snp.txt | awk '$5 + $6 < 300' | awk '{ print $1,$2,$3,$4,$5,$6,$9,$10,$15 }' | sed 's/\ /,/g' > "$OUTSTART"_snp_covlt300.csv

'''