

#calss header
class _SMARMY():
	def __init__(self,): 
		self.name = "SMARMY"
		self.definitions = [u'extremely polite or helpful or showing a lot of respect in a way that is annoying or does not seem sincere: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
