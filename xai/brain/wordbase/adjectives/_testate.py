

#calss header
class _TESTATE():
	def __init__(self,): 
		self.name = "TESTATE"
		self.definitions = [u'(of a person) having left a will (= document saying who should get their possessions)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
