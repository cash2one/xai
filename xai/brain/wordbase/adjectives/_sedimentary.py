

#calss header
class _SEDIMENTARY():
	def __init__(self,): 
		self.name = "SEDIMENTARY"
		self.definitions = [u'(of rock) made from sediment left by the action of water, ice, or wind: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
