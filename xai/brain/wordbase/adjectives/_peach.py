

#calss header
class _PEACH():
	def __init__(self,): 
		self.name = "PEACH"
		self.definitions = [u'having a pale colour between pink and orange']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
