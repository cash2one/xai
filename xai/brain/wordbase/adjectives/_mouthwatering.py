

#calss header
class _MOUTHWATERING():
	def __init__(self,): 
		self.name = "MOUTHWATERING"
		self.definitions = [u'Mouthwatering food looks as if it will taste good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
