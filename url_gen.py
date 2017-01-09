templ = 'ftp://ftp.ncbi.nlm.nih.gov/pubmed/baseline/medline17n0%s.xml.gz'
for i in range(1, 892 + 1):
    cmd = templ % str(i).zfill(3)
    print(cmd)