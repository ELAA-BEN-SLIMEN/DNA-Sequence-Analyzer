import requests
import matplotlib.pyplot as plt


# 1. Validate DNA sequence
def validate_dna(sequence):
    valid_nucleotides = "ATGC"

    if len(sequence) == 0:
        return False

    for nucleotide in sequence:
        if nucleotide not in valid_nucleotides:
            return False

    return True


# 2. Read FASTA file from GitHub
def read_fasta():
    url = (
        "https://raw.githubusercontent.com/"
        "ELAA-BEN-SLIMEN/DNA-Sequence-Analyzer/"
        "main/sample.fasta"
    )

    response = requests.get(url, timeout=15)
    response.raise_for_status()

    lines = response.text.splitlines()

    dna = "".join(
        line.strip()
        for line in lines
        if line.strip() and not line.startswith(">")
    )

    return dna


# 3. Analyze DNA sequence
def analyze_dna(dna):
    if not validate_dna(dna):
        raise ValueError("Invalid DNA sequence!")

    print("DNA validation successful!")
    print("DNA sequence:", dna)
    print("Sequence length:", len(dna))

    a = dna.count("A")
    t = dna.count("T")
    g = dna.count("G")
    c = dna.count("C")

    gc_percentage = (g + c) / len(dna) * 100

    print("Number of A:", a)
    print("Number of T:", t)
    print("Number of G:", g)
    print("Number of C:", c)
    print("GC percentage:", round(gc_percentage, 2), "%")

    return [a, t, g, c]


# 4. Visualize nucleotide distribution
def plot_nucleotides(counts):
    nucleotides = ["A", "T", "G", "C"]

    plt.bar(nucleotides, counts)
    plt.title("DNA Nucleotide Distribution")
    plt.xlabel("Nucleotides")
    plt.ylabel("Frequency")
    plt.show()


# 5. Compare two DNA sequences
def compare_sequences(dna1, dna2):
    if not validate_dna(dna1) or not validate_dna(dna2):
        raise ValueError("Invalid DNA sequence!")

    if len(dna1) != len(dna2):
        raise ValueError("Sequences must have equal lengths!")

    differences = 0

    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            differences += 1
            print("Difference at position:", i + 1)
            print(dna1[i], "->", dna2[i])

    print("Total differences:", differences)

    return differences


# 6. Main program
def main():
    dna = read_fasta()

    counts = analyze_dna(dna)

    plot_nucleotides(counts)

    dna1 = "ATGCGATC"
    dna2 = "ATGTGATC"

    compare_sequences(dna1, dna2)


if __name__ == "__main__":
    main()

            
