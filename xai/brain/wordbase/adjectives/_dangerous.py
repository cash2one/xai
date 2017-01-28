

#calss header
class _DANGEROUS():
	def __init__(self,): 
		self.name = "DANGEROUS"
		self.definitions = [u'A dangerous person, animal, thing, or activity could harm you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
