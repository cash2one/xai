

#calss header
class _SITUATED():
	def __init__(self,): 
		self.name = "SITUATED"
		self.definitions = [u'in a particular position: ', u'in a particular situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
