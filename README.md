osgen
=====

Open Source GENome Tool Component:
Disease XML Files + python parsing code
opensourcegenome.org

=====

Information about each disease and associated SNPs is stored in an XML file. This allows the disease and SNP information to be under source control and is platform agnostic. Files can be changed or added to the repository by contributers, and others can build platforms to analyze their genome using the XML files. For instance, for a web app, the XML files could be loaded into a database, or interpreted by javascript in the browser. They could also be interpreted by a local script. 

Python code is included to parse the XML files locally. 

====

How things are so far:

Currently there are two different types of output possible, phenotype (a description of a trait resulting from a certain genotype) or probability, an adjusted odds ratio given one or multiple SNPs or alleles influencing the probability of having a trait. 

Theoretically the same snp/trait could be presented in both ways. For instance, 23andme has one SNP for eye color and they present different phenotypes based on that one SNP. However there are multiple known SNPs that influence eye color. An eye color file could, for instance, only present the probability of having brown eyes as a function of multiple SNPs/alleles. 

This is the example demonstrated in the probability.xml and phenotype.xml files in /xml schemas/
