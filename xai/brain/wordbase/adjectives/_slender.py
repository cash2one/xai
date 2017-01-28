

#calss header
class _SLENDER():
	def __init__(self,): 
		self.name = "SLENDER"
		self.definitions = [u'thin and delicate, often in a way that is attractive: ', u'small in amount or degree: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
