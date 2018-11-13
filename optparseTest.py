import optparse

parser = optparse.OptionParser('usage %prog -H <target host> -p <target port>')
parser.add_option('-H', dest = 'tgtHost', type = 'string', help='specify target host')
parser.add_option('-p', dest = 'tgtPort', type = 'int', help='specify target port')
option, args = parser.parse_args()
print(option, args)
