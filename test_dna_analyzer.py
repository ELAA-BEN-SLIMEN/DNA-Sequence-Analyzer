from dna_analyzer import validate_dna

def test_valid_dna():
    assert validate_dna("ATGC") is True

def test_invalid_dna():
    assert validate_dna("ATGCX") is False

def test_empty_dna():
    assert validate_dna("") is False

def test_numbers():
    assert validate_dna("ATG123") is False
    
from dna_analyzer import (
    read_fasta_sequences,
    analyze_multiple_sequences
)

def test_multiple_fasta():
    text = ">seq1\nATGC\n>seq2\nGGCC"
    sequences = read_fasta_sequences(text)

    assert len(sequences) == 2
    assert sequences["seq1"] == "ATGC"
    assert sequences["seq2"] == "GGCC"


def test_gc_percentage():
    sequences = {
        "seq1": "ATGC",
        "seq2": "GGCC"
    }

    df = analyze_multiple_sequences(sequences)

    assert df.loc[0, "GC (%)"] == 50.0
    assert df.loc[1, "GC (%)"] == 100.0


def test_invalid_multiple_sequence():
    sequences = {"seq1": "ATGX"}

    try:
        analyze_multiple_sequences(sequences)
        assert False, "Expected ValueError"
    except ValueError:
        pass

