

#calss header
class _QUADRUPLE():
	def __init__(self,): 
		self.name = "QUADRUPLE"
		self.definitions = [u'four times as big: ', u'involving four parts, people, places, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
