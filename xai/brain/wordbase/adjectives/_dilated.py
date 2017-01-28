

#calss header
class _DILATED():
	def __init__(self,): 
		self.name = "DILATED"
		self.definitions = [u'wider or further open than usual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
