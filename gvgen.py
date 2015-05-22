from subprocess import call

dotpath = 'dot.exe' #change this if graphviz is not in path.
#filename = 'test.dot'
#outputname = 'o.svg'

def gvgen(filename, outputname, dotpath = dotpath):
	call(dotpath + ' -Tsvg ' + filename + ' -o ' + outputname)

#gvgen(filename, outputname)