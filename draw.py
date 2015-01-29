'''
Usage:
    draw.py <count> <fn_list>
'''

import random
import docopt

if __name__ == '__main__':
    args = docopt.docopt(__doc__)
    a = open(args['<fn_list>']).read().splitlines()
    a = sorted(a)
    random.seed(' '.join(a))
    random.shuffle(a)
    print('You get tickets:', a[:int(args['<count>'])])

