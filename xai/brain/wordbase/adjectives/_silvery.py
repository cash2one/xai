

#calss header
class _SILVERY():
	def __init__(self,): 
		self.name = "SILVERY"
		self.definitions = [u'like silver: ', u'having a pleasant, clear musical sound: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
