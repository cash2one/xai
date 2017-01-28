

#calss header
class _EQUIVOCAL():
	def __init__(self,): 
		self.name = "EQUIVOCAL"
		self.definitions = [u'not clear and seeming to have two opposing meanings, or confusing and able to be understood in two different ways: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
