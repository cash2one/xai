

#calss header
class _ADAPTIVE():
	def __init__(self,): 
		self.name = "ADAPTIVE"
		self.definitions = [u'having an ability to change to suit different conditions']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
