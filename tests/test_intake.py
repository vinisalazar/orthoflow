

def test_extract_cds_MH591083(run_workflow):
    w = run_workflow("results/intake/cds/MH591083-truncated.cds.fa")
    w.assert_contains(">Flabellia_petiolata_HV01202|MH591083-truncated.gb|0|petG")


def test_extract_cds_KY819064(run_workflow):
    w = run_workflow("results/intake/cds/KY819064-truncated-cds.cds.fa")
    w.assert_contains(">Chlorodesmis_fastigiata_HV03865|KY819064-truncated.cds.fasta|0")


def test_translate(run_workflow):
    w = run_workflow("results/intake/translated/NC_026795-truncated.protein.fa")
    w.assert_contains("MSIQISLRQFINKSINTLFLCGIFLYANPQDTFAYPIFAQQNYENPREPNGRLVCANCHL")

def test_protein(run_workflow):
    w = run_workflow("results/intake/protein/protein_intake.protein.fa", "--files", "protein_intake.fa", "--config", "infer_tree_with_cds_seqs=0", "ignore_non_valid_files=1")
    w.assert_contains("MPVTKKPDLSDIFLRKKLSKGMGHHYYGEPAWPNELLYIFPVCIVGIFGCVIGLAILDPA")
