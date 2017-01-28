

#calss header
class _THERMOPLASTIC():
	def __init__(self,): 
		self.name = "THERMOPLASTIC"
		self.definitions = [u'Thermoplastic substances can be melted and formed into shapes that become hard, and can then be melted again.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
