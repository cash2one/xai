

#calss header
class _SOLICITOUS():
	def __init__(self,): 
		self.name = "SOLICITOUS"
		self.definitions = [u'showing care and helpful attention to someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
