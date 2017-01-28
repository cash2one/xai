

#calss header
class _INDEBTED():
	def __init__(self,): 
		self.name = "INDEBTED"
		self.definitions = [u'grateful because of help given: ', u'owing money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
