

#calss header
class _CONNOTATIVE():
	def __init__(self,): 
		self.name = "CONNOTATIVE"
		self.definitions = [u'The connotative meaning of a word includes the feelings and ideas that people may connect with that word.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
