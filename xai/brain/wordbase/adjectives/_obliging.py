

#calss header
class _OBLIGING():
	def __init__(self,): 
		self.name = "OBLIGING"
		self.definitions = [u'willing or eager to help: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
