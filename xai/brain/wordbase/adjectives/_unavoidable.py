

#calss header
class _UNAVOIDABLE():
	def __init__(self,): 
		self.name = "UNAVOIDABLE"
		self.definitions = [u'impossible to avoid']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
