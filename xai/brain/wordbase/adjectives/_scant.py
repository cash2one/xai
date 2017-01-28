

#calss header
class _SCANT():
	def __init__(self,): 
		self.name = "SCANT"
		self.definitions = [u'very little and not enough: ', u'almost: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
