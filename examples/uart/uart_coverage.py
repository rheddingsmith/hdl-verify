from hdl_verify.coverage import Coverage

class UartCoverage(Coverage):
    def register_bins(coverage):

        for i in range(8):

            coverage.add_bin(f'bit_{i}_high')
            coverage.add_bin(f'bit_{i}_low')

        coverage.add_bin('all_zeros')
        coverage.add_bin('all_ones')
        coverage.add_bin('alternating')


    def sample_bins(coverage, transaction):

        for i in range(8):

            if (transaction.data >> i) & 1:

                coverage.sample(f'bit_{i}_high')

            else:

                coverage.sample(f'bit_{i}_low')

        if(transaction.data == 0):

            coverage.sample('all_zeros')
    
        if(transaction.data == 0xFF):

            coverage.sample('all_ones')

        if(transaction.data == 0x55 or transaction.data == 0xAA):

            coverage.sample('alternating')




