

#calss header
class _NAUSEOUS():
	def __init__(self,): 
		self.name = "NAUSEOUS"
		self.definitions = [u'feeling as if you might vomit: ', u'making you feel as if you might vomit: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
