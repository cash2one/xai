

#calss header
class _TURNKEY():
	def __init__(self,): 
		self.name = "TURNKEY"
		self.definitions = [u'(of a piece of equipment) ready to be used immediately by the person who is buying or renting it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
