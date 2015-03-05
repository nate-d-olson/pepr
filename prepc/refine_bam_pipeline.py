def main(accession, ref, accession_params):
    ''' Processing single bam file'''
    import bwa_commands
    import samtools_commands
    import picard_commands
    import gatk_commands
    if accession_params['plat'] == "miseq":
        picard_commands.bam_group_sort(in_bam = accession_params['sorted_bam'], 
         out_bam = accession_params['group_sort_file'], 
         log_dir = accession_params['mapping_log'])
        
        picard_commands.bam_fixmate(in_bam = accession_params['group_sort_file'],
            out_bam = accession_params['fix_file'],
            log_dir = accession_params['mapping_log'])
        bam_file = accession_params['fix_file']
    else:
    	bam_file = accession_params['sorted_bam']
        # run as part of mapping pipeline
        # bam_sort(in_bam = accession_params['fix_file'], 
        #         out_sort = accession_params['sort_file'], 
        #         out_dir = accession_params['log_dir'])
    # else:
    #     bam_add_header(in_bam=accession_params['bam'], 
    #                    out_header=accession_params['header_file'],
    #                    log_dir=accession_params['log_dir'],
    #                    read_group=accession_params['read_group'])

    #     bam_sort(in_bam = accession_params['header_file'], 
    #             out_sort = accession_params['sort_file'], 
    #             out_dir = accession_params['log_dir'],
    #             intervals_file = accession_params['intervals_file'],
    #             log_dir = accession_params['log_dir'])
    # note no realign step ....
    gatk_commands.gatk_realign(in_ref=ref,
        in_bam=bam_file,
        out_bam=accession_params['realign_file'],
        intervals_file=accession_params['intervals_file'],
        log_dir=accession_params['mapping_log'])

    picard_commands.bam_markdup(in_bam = accession_params['realign_file'], 
        out_bam = accession_params['markdup_file'], 
        metrics_file = accession_params['metrics_file'],
        log_dir = accession_params['mapping_log'])
    
    samtools_commands.samtools_bam_index(in_bam = accession_params['markdup_file'], 
        log_dir = accession_params['mapping_log'])


# def genome_pileups(analysis_params):    
#     for plat in ["miseq", "pgm"]:
#         out_dir = pipeline_params['root_dir'] + pipeline_params['analysis_out_dir']
#         vcf = out_dir + "/" + pipeline_params['RM'] + "-" + plat + ".vcf"
#         genome_calls_mpileup(bams=markdup_files[plat],
#                              ref=pipeline_params['ref'],
#                              vcf_file=vcf,log_dir=out_dir)