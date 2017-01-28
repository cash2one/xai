

#calss header
class _SALUTARY():
	def __init__(self,): 
		self.name = "SALUTARY"
		self.definitions = [u'causing improvement of behaviour or character: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
