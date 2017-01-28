

#calss header
class _SPASTIC():
	def __init__(self,): 
		self.name = "SPASTIC"
		self.definitions = [u'suffering from cerebral palsy (= a condition of the body that makes it difficult to control the muscles)', u'an offensive way of saying "stupid", used especially by children']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
