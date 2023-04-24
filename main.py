import os
import yaml
from package.whmsft import oranje

cwd = os.getcwd()
pdir = os.path.dirname(os.path.realpath(__file__))

PACKAGE = {}
"""
How the "PACKAGE" dict will look like:
PACKAGE = {
	'whmsft': {
		'oranje': {...} # With all data in `data.yml`
		}
	}
}
"""

if __name__ == "__main__":
	for author in os.listdir(f'{pdir}/package'):
		if os.path.isdir(f'{pdir}/package/{author}'):
			PACKAGE[author] = []
	for author in PACKAGE.keys():
		for pack in os.listdir(f'{pdir}/package/{author}'):
			if (os.path.isdir(f'{pdir}/package/{author}/{pack}')):
				if not (author == "whmsft" and pack == "oranje"):
					PACKAGE[author][pack] = yaml.safe_load(open(f'{pdir}/package/{author}/{pack}/data.yml').read())
					exec(f'import package.{author}.{pack}')
					taskList = PACKAGE[author][pack]['tasks']
					if ('initialize' in taskList) and (taskList['initialize'] != None):
						exec(f'package.{author}.{pack}.{taskList["initialize"]}')
					del taskList
	
	for author in PACKAGE.keys():
		for pack in author.keys():
			taskList = PACKAGE[author][pack]['tasks']
			if ('beforeLoop' in taskList) and (taskList['beforeLoop'] != None):
				exec(f'package.{author}.{pack}.{taskList["beforeLoop"]}')
			del taskList
	oranje.editor.mainloop()
	for author in PACKAGE.keys():
		for pack in author.keys():
			taskList = PACKAGE[author][pack]['tasks']
			if ('afterLoop' in taskList) and (taskList['afterLoop'] != None):
				exec(f'package.{author}.{pack}.{taskList["afterLoop"]}')
			del taskList