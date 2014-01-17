import csv, re

def loadgen():
    '''
    Creates a dictionary rsid_dict where the key is the rsid and the value is the genotype at that location. 
    '''
    with open("sample genomes/23andme_sample.txt", 'rb') as f:
        genome= csv.reader(f, delimiter='	')
        rsid_pattern = re.compile(r'^rs[0-9]+$')
        genotype_pattern = re.compile(r'^[AGTC]{2}$')
        rsid_dict = {}
        for row in genome:
            if len(row) == 4: #valid lines of a 23andme file should have 4 columns
                rsid_match = rsid_pattern.match(row[0]) #valid lines of a 23andme file should match the pattern of an rsid in the first column
                genotype_match = genotype_pattern.match(row[3]) #valid lines of a 23andme file should match the pattern of a genotype in the 4th column
                
                if rsid_match and genotype_match:
                    '''
                    Hopefully this will be robust against manually corrupted files- for instance, user inserted spaces should cause
                    the entire line to be rejected. And if the user inserted space is a tab, the rsid and genotypes won't be in the correct position,
                    and again, the line will be rejected.
                    
                    Please fix this if you can make it more robust. It's better to reject an entire line than to potentially report false genotypes!
                    '''
                    #print rsid_match.group() #should be your rsid
                    #print genotype_match.group() #should be your corresponding genotype
                    
                    rsid_dict[rsid_match.group()] = genotype_match.group()
        #print rsid_dict
                    
if  __name__ =='__main__':
    loadgen()
