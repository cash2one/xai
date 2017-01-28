

#calss header
class _UNEDUCATED():
	def __init__(self,): 
		self.name = "UNEDUCATED"
		self.definitions = [u'having received little or no education']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
