from pathlib import Path

def test_orthofisher_input_generation(run_workflow):
    w = run_workflow("results/orthofisher/input_protein_files.tsv", expected_dir=Path(__file__).parent/"test-data")
    w.assert_contains("results/intake/translated/KY509313.protein.fa")
    w.assert_contains("results/intake/translated/MH591083.protein.fa")


def test_orthofisher(run_workflow):
    w = run_workflow("results/orthofisher/output", expected_dir=Path(__file__).parent/"test-data")
    w.assert_dir_exists()
    # w.assert_contains(
    #     "KY509313.protein.fa	1080at3041.hmm	single-copy	1	Avrainvillea_mazei_HV02664|0|KY509313.1|ftsH",
    #     expected_files="results/orthofisher/output/long_summary.txt",
    # )


def test_min_seq_filter_orthofisher(run_workflow):
    w = run_workflow("results/orthofisher/min-seq-filtered", expected_dir=Path(__file__).parent/"test-data")
    w.assert_dir_exists()
    # w.assert_glob_count("*.fa", min=15)

