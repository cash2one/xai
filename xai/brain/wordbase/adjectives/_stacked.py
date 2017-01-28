

#calss header
class _STACKED():
	def __init__(self,): 
		self.name = "STACKED"
		self.definitions = [u'covered or filled with a large amount of things: ', u'(of a woman) having large breasts. This sense is considered offensive by many women.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
