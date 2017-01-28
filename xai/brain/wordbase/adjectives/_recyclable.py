

#calss header
class _RECYCLABLE():
	def __init__(self,): 
		self.name = "RECYCLABLE"
		self.definitions = [u'able to be recycled']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
