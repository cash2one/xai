

#calss header
class _PASTEL():
	def __init__(self,): 
		self.name = "PASTEL"
		self.definitions = [u'having a pale soft colour: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
