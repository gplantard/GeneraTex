import argparse
import os
import subprocess

def saveTeXFile(teXcontent, fileName = "temp.tex", templateFile='template.tex'):
    templateContent=r"""
    \documentclass{article}
    \begin{document}
    %(content)
    \end{document}
    """
    if(templateFile!=""):
        print("-----------------------------------------------------------------------")
        print("!- Be sure that your template file contain '%(content)' in the text -!")
        print("-----------------------------------------------------------------------")
        with open(templateFile, 'r') as content_file:
            templateContent = content_file.read()

    content = templateContent.replace('%(content)', teXcontent)
    with open(fileName,'w') as f:
        f.write(content)

def compileTexFile(filename = "temp.tex"):
    fileNameWoExt = filename.split(".tex")[0]
    cmd = ['pdflatex', '-interaction', 'nonstopmode', filename]
    proc = subprocess.Popen(cmd)
    proc.communicate()

    retcode = proc.returncode
    if not retcode == 0:
        os.unlink(fileNameWoExt+'.pdf')
        raise ValueError('Error {} executing command: {}'.format(retcode, ' '.join(cmd)))

    os.unlink(filename)
    os.unlink(fileNameWoExt+'.log')

"""
import sys
import re
import subprocess

template = file('template.tex', 'r').read()
pattern = re.compile('%\(([^}]+)\)[bcdeEfFgGnosxX%]')
tokens = pattern.findall(template)

token_values = dict()
for token in tokens:
    sys.stdout.write('Enter value for ' + token + ': ')
    token_values[token] = sys.stdin.readline().strip()

page = template % token_values
file('result.tex', 'w').write(page)

subprocess.call('pdflatex result.tex')
"""