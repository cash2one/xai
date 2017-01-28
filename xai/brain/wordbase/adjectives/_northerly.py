

#calss header
class _NORTHERLY():
	def __init__(self,): 
		self.name = "NORTHERLY"
		self.definitions = [u'towards or in the north: ', u'a wind that comes from the north']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
