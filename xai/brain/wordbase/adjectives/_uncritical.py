

#calss header
class _UNCRITICAL():
	def __init__(self,): 
		self.name = "UNCRITICAL"
		self.definitions = [u'accepting something too easily, because of being unwilling or unable to criticize: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
