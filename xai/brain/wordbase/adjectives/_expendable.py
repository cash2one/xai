

#calss header
class _EXPENDABLE():
	def __init__(self,): 
		self.name = "EXPENDABLE"
		self.definitions = [u'If someone or something is expendable, people can do something or deal with a situation without them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
