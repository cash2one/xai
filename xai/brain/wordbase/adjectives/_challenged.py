

#calss header
class _CHALLENGED():
	def __init__(self,): 
		self.name = "CHALLENGED"
		self.definitions = [u'having a physical or mental condition that makes ordinary activities more difficult than they are for other people']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
