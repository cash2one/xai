

#calss header
class _MINDLESS():
	def __init__(self,): 
		self.name = "MINDLESS"
		self.definitions = [u'stupid and meaning nothing: ', u'not needing much mental effort: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
