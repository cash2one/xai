

#calss header
class _OVERWORKED():
	def __init__(self,): 
		self.name = "OVERWORKED"
		self.definitions = [u'having to work too much: ', u'used to describe language that has been used too much and has lost its meaning: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
