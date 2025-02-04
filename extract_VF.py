input_file='AllGenes.txt'
output_file='AllvF.fasta'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    fasta_id = None
    protein_sequence = None
    collecting_sequence = False

    for line in infile:
        line = line.strip()
        if line.startswith("UniProtID:"): # find the protein ID and store it for the fasta file
            if fasta_id and protein_sequence: # if there is an unsaved entry, write it to the file
                outfile.write(f">{fasta_id}\n{protein_sequence}\n")
            fasta_id = line.split(":")[1].strip() # split the line by : and store the name bit
            protein_sequence = "" # reset the protein sequence
            collecting_sequence = False # reset the collecting sequence flag to skip the nonsense
        elif line.startswith("Protein Sequence:"): # if the line starts with protein sequence...
            collecting_sequence = True # ...start collecting the sequence
        elif collecting_sequence:
            if line == "": # keep collecting the sequence until we reach an empty line
                collecting_sequence = False # stop collecting the sequence
            else:
                line = line.translate(str.maketrans('', '', '0123456789\t ')) # Remove numbers, spaces and tabs from the sequence
                protein_sequence += line # next line
    
    # Make sure to write the last entry if exists
    if fasta_id and protein_sequence:
        outfile.write(f">{fasta_id}\n{protein_sequence}\n")
