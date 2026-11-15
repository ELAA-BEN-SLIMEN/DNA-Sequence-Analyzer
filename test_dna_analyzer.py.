from dna_analyzer import validate_dna

def test_valid_dna():
    assert validate_dna("ATGC") is True

def test_invalid_dna():
    assert validate_dna("ATGCX") is False

def test_empty_dna():
    assert validate_dna("") is False

def test_numbers():
    assert validate_dna("ATG123") is False
