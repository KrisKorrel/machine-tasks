input_file = open("test_output_symbol_eos/grammar_std.train.full.tsv", 'r')
output_file1 = open("test_output_symbol_eos/bla.tsv", 'w')

n = 100000 / 10
i = 0
for line in input_file:
    if i < n:
        pass
    else:
        output_file1.write(line)

    i += 1