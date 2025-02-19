def test_mafft(run_workflow):
    w = run_workflow("results/alignment/aligned_proteins/OG0000000_orthosnap_0.protein.alignment.fa")
    w.assert_contains(">Caulerpa_cliftonii_HV03798|KX808498-truncated.gb|28|psbE")
    w.assert_contains("TDRLNALKQINKNL---")


def test_get_cds_seq(run_workflow):
    w = run_workflow("results/alignment/seqs_cds/OG0000001.cds.seqs.fa")
    w.assert_contains(">Caulerpa_cliftonii_HV03798|KX808498-truncated.gb|22|rpl23")
    w.assert_contains("ATGTTTGATTTTTTAAATAAACCATTAATAACAGAAAAAGCAACTCAACTTATTGAA")


def test_taxon_only(run_workflow):
    w = run_workflow("results/alignment/taxon_only/OG0000003.taxon_only.protein.alignment.fa")
    w.assert_contains(">Caulerpa_cliftonii_HV03798\n")
    w.assert_contains(">Avrainvillea_mazei_HV02664\n")
    w.assert_contains(">Chlorodesmis_fastigiata_HV03865\n")


def test_thread_dna(run_workflow):
    w = run_workflow("results/alignment/threaded_cds/OG0000002.cds.alignment.fa")
    w.assert_contains(">Caulerpa_cliftonii_HV03798\n")
    w.assert_contains("ATGTTTTGTAAACACAAAAAATCTAAAGATCAATTCTTTTTAACATGTGGA-----")


def test_trim_alignments(run_workflow):
    w = run_workflow("results/alignment/trimmed_cds/OG0000003.trimmed.cds.alignment.fa")
    w.assert_contains(">Caulerpa_cliftonii_HV03798\n")
    w.assert_contains("ATGACCGCAGCATATTTACCTCAAATTTTCGTGCCACTCGTTGGTTTATTTTTTCCGCTT")


def test_list_alignments(run_workflow):
    w = run_workflow("results/alignment/alignments_list.protein.txt")
    w.assert_contains("results/alignment/trimmed_protein/OG0000002.trimmed.protein.alignment.fa\n")
    w.assert_contains("results/alignment/trimmed_protein/OG0000005.trimmed.protein.alignment.fa\n")    


def test_list_alignments_cds(run_workflow):
    w = run_workflow("results/alignment/alignments_list.cds.txt")
    w.assert_contains("results/alignment/trimmed_cds/OG0000002.trimmed.cds.alignment.fa\n")
    w.assert_contains("results/alignment/trimmed_cds/OG0000005.trimmed.cds.alignment.fa\n")    



