

#calss header
class _ACCUMULATIVE():
	def __init__(self,): 
		self.name = "ACCUMULATIVE"
		self.definitions = [u'gradually increasing in number or amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
