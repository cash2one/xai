

#calss header
class _ROMAN():
	def __init__(self,): 
		self.name = "ROMAN"
		self.definitions = [u'Roman letters are in the ordinary style of printed writing in which the letters are vertical.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
