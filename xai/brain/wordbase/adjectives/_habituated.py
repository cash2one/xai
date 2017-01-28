

#calss header
class _HABITUATED():
	def __init__(self,): 
		self.name = "HABITUATED"
		self.definitions = [u'used to something, especially something unpleasant: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
