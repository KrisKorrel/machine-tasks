fin = open('heldout_tables.tsv')
fout1 = open('heldout_tables_sn.tsv', 'w')
fout2 = open('heldout_tables_ns.tsv', 'w')

for line in fin:
    s = line.split(' ')
    if '7' in s[1] or '8' in s[1]:
        fout2.write(line)
    else:
        fout1.write(line)