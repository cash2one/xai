

#calss header
class _PALPABLE():
	def __init__(self,): 
		self.name = "PALPABLE"
		self.definitions = [u'so obvious that it can easily be seen or known, or (of a feeling) so strong that it seems as if it can be touched or physically felt: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
