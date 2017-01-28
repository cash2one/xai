

#calss header
class _MESSIANIC():
	def __init__(self,): 
		self.name = "MESSIANIC"
		self.definitions = [u'relating or belonging to a messiah: ', u'A messianic religious group believes that a leader will or has come who has the power to change the world and bring peace: ', u'A messianic speech or style is very determined and full of emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
