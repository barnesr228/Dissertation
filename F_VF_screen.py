with open("FVFTblastnNoDuplicates.txt", "r") as IDFile, \
     open("AllVF.fasta", "r") as SeqFile, \
     open("FVFCat.fa", "w") as OutFile:
    
    # create dictionary for fasta seq
    fasta_dict = {} 
    current_header = None # current ID
    current_sequence = [] 

    for line in SeqFile: 
        line = line.strip() # remove new line
        if line.startswith(">"): # check if ID line
            if current_header:
                fasta_dict[current_header] = "".join(current_sequence) # add to dictionary
            current_header = line[1:]  # remove ">"
            current_sequence = [] # reset 
        else:
            current_sequence.append(line)
    
    # add last seq
    if current_header:
        fasta_dict[current_header] = "".join(current_sequence)
    
    # write matching IDs to seq 
    for id_line in IDFile:
        id = id_line.strip()
        if id in fasta_dict:
            OutFile.write(f">{id}\n{fasta_dict[id]}\n")
