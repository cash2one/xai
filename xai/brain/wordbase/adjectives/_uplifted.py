

#calss header
class _UPLIFTED():
	def __init__(self,): 
		self.name = "UPLIFTED"
		self.definitions = [u'raised: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
