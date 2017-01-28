

#calss header
class _LILAC():
	def __init__(self,): 
		self.name = "LILAC"
		self.definitions = [u'having a pale colour between pink and purple']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
