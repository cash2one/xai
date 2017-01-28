

#calss header
class _FEEDER():
	def __init__(self,): 
		self.name = "FEEDER"
		self.definitions = [u'used to refer to something that leads to or supplies a larger thing of the same type: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
