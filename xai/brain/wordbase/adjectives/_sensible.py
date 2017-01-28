

#calss header
class _SENSIBLE():
	def __init__(self,): 
		self.name = "SENSIBLE"
		self.definitions = [u'based on or acting on good judgment and practical ideas or understanding: ', u'Sensible clothes or shoes are practical and suitable for the purpose they are needed for, rather than being attractive or fashionable: ', u'having an understanding of a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
