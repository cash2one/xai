

#calss header
class _AMBIENT():
	def __init__(self,): 
		self.name = "AMBIENT"
		self.definitions = [u'(especially of environmental conditions) existing in the surrounding area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
