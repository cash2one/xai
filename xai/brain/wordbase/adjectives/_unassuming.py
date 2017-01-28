

#calss header
class _UNASSUMING():
	def __init__(self,): 
		self.name = "UNASSUMING"
		self.definitions = [u'Someone who is unassuming is quiet and shows no wish for attention or admiration: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
