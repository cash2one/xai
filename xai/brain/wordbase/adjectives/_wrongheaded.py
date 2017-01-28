

#calss header
class _WRONGHEADED():
	def __init__(self,): 
		self.name = "WRONGHEADED"
		self.definitions = [u'based on ideas or judgments that are not suitable for a particular situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
