import jinja2
import codecs
import glob

def generateCode(CURRENT_TEMPLATE_FILE):
	templateLoader = jinja2.FileSystemLoader( searchpath="." )
	templateEnv = jinja2.Environment( loader=templateLoader )
	template = templateEnv.get_template( CURRENT_TEMPLATE_FILE )
	COLUMNS       = [tuple(line.split(':')) for line in codecs.open( "InputData.txt", "r", "utf-8" )] #open('Tlist.txt')]
	#if inputData is of type columnName:Column Description
	try:
		COLUMNS       = map(lambda s: (s[0],(s[0].strip().title(),s[1].strip())), COLUMNS)
	#if inputData is of type columnName
	except IndexError:
		COLUMNS       = map(lambda s: (s[0],(s[0].strip().title(),s[0].strip().lower())), COLUMNS)
	#ignore first line 
	COLUMNS.pop(0)
	templateVars  = [tuple(line.split(':')) for line in codecs.open( "InputVariables.txt", "r")] 
	templateVars  = map(lambda s: (s[0],(s[0].strip(),s[1].strip())), templateVars)
	#ignore first line 
	templateVars.pop(0)
	templateVars  = {x[1][0]:x[1][1] for x in templateVars}
	templateVars.update({"columns" : COLUMNS})  
	print templateVars
	outputText = template.render( templateVars )
	output_file_name = CURRENT_TEMPLATE_FILE.replace('.jinja','.txt').replace('Template_','out_')
	f = open(output_file_name, 'w')
	#f = open('out_' + templateVars['table']+'.txt', 'w')
	outputText = outputText.encode('utf-8')
	f.write(outputText)
	f.close()
	#print outputText

myTemplateList = [f for f in glob.glob("Template_*.jinja")]
print myTemplateList
for CURRENT_TEMPLATE_FILE in myTemplateList: 
	generateCode(CURRENT_TEMPLATE_FILE)
