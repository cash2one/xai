

#calss header
class _SUCCESSIVE():
	def __init__(self,): 
		self.name = "SUCCESSIVE"
		self.definitions = [u'happening one after the other without any break: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
