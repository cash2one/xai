

#calss header
class _ILLEGITIMATE():
	def __init__(self,): 
		self.name = "ILLEGITIMATE"
		self.definitions = [u'born of parents not married to each other', u'not legal or fair: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
