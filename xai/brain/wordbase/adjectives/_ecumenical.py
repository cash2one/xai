

#calss header
class _ECUMENICAL():
	def __init__(self,): 
		self.name = "ECUMENICAL"
		self.definitions = [u'encouraging the different Christian Churches to unite: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
