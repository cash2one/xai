

#calss header
class _INCESSANT():
	def __init__(self,): 
		self.name = "INCESSANT"
		self.definitions = [u'never stopping, especially in an annoying or unpleasant way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
