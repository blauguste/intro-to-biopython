from Bio import SeqIO
from Bio import Entrez

def ct_features():
    
    # User inputs
    name = input("\nYour name: \n")
    gb = input("\nAccession of genome to be analyzed: \n")
    foi = input("\nType of feature to find: \n")
    email = input("\nYour email address: \n")

    # Get record from NCBI
    Entrez.email = email
    print("\nFetching record from NCBI... ")
    ef = Entrez.efetch(db='nucleotide', id=gb, \
        rettype='gbwithparts', retmode='text')

    # Parse record from NCBI
    with ef as handle:
        rec = SeqIO.read(handle, 'genbank')
        fct = 0
        fct_compl = 0
        for f in rec.features:
            if f.type == foi:
                fct += 1
                if f.strand == -1:
                    fct_compl += 1
    
    # Write results to file
    ofn = name + '_HW.txt'
    congrats = "Congratulations %s, you beautiful genius!" \
        "\n\nResults written to file: %s" % (name, ofn)
    analysis = "Successfully analyzed %s: %s for %ss. " \
        "\n\nThis genome has %i %s features. %i are on the complement strand." \
        % (rec.id, rec.description, foi, fct, foi, fct_compl)
    
    print("\n\n" + analysis + "\n\n")
    print(congrats)
    
    with open(ofn, 'w') as outfile:
        outfile.write(analysis + "\n\n")