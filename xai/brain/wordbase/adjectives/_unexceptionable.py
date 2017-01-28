

#calss header
class _UNEXCEPTIONABLE():
	def __init__(self,): 
		self.name = "UNEXCEPTIONABLE"
		self.definitions = [u'not bad; having nothing that anyone could criticize or disapprove of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
