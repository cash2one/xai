

#calss header
class _INGRATIATING():
	def __init__(self,): 
		self.name = "INGRATIATING"
		self.definitions = [u'Ingratiating behaviour is intended to make people like you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
