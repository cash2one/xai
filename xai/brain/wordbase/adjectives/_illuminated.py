

#calss header
class _ILLUMINATED():
	def __init__(self,): 
		self.name = "ILLUMINATED"
		self.definitions = [u'An illuminated text is decorated with added colour, gold paint, and small pictures, as was often done in the Middle Ages (= between about AD 1000 and AD 1500): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
