#!/usr/bin/env python2.5
# by weakish <weakish@gmail.com>, licensed under GPL v2.

'''Markup characters need manual checks.'''




helpinfo = '''stupidm -- Markup characters need manual checks

Usage:

cat infile | stupidm table starttag endtag > outfile
stupidm -h # print this help page

Example:

table.txt
fb
iopt

$ echo 'hi, foo' | stupidm table.txt '{' '}'
hi{opt}, f{b}oo

'''


def main():
    import sys
    if len(sys.argv) < 2:
        print helpinfo
        sys.exit(2)
    else:
        if sys.argv[1] == '-h':
            print helpinfo
            sys.exit()
        else:
            text = unicode(sys.stdin.read(), 'utf-8')
            table = gen_table(sys.argv[1])
            pre, post = sys.argv[2], sys.argv[3]
            print markup(text, table, pre, post).encode('utf-8')

def markup(text, table, pre, post):

    def mark(char):
        return (char + pre + table[char] + post) if (char in table) else char

    return ''.join(mark(char) for char in text)


def gen_table(file):
    import codecs
    table = codecs.open(file, 'r', encoding='utf-8')
    return dict((line[0],line[1:].rstrip('\n')) for line in table.readlines())
    

if __name__  == '__main__':
    main()
