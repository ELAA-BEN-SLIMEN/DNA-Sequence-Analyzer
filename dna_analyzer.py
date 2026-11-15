dna="ATGCGATCGATC"
print("DNA sequence:",dna)
print("sequence length:",len(dna))
g=dna.count("G")
c=dna.count("C")
gc_percentage=((g+c)/len(dna))*100
print("Number of G:",g)
print("Number of c:",c)
print("Gc percentage:",round(gc_percentage,2),"%")
a=dna.count("A")
t=dna.count("T")
print("Number of A:",a)
print("Number of T:",t)
print("Number of G:",g)
print("Number of C:",c)
import matplotlib.pyplot as plt
nucleaotides=["A","T","G","C"]
counts=[a,t,g,c]
plt.bar(nucleaotides,counts)
plt.title("DNA Nucleotide Distribution")
plt.xlabel("Nucleaotides")
plt.ylabel("Frequency")
plt.show()
dna1="ATGCGATC"
dna2="ATGTGATC"
mutations=0
for i in range(len(dna1)):
  if dna1[i]!=dna2[i]:
    mutations+=1
    print("Difference at position:",i+1)
    print(dna1[i],'->',dna2[i])
print("Total differences:",mutations)

      
            
            
            
