

#calss header
class _TAKEN():
	def __init__(self,): 
		self.name = "TAKEN"
		self.definitions = [u'believing something to be deserving of respect or admiration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
