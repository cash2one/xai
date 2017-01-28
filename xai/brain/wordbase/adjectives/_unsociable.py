

#calss header
class _UNSOCIABLE():
	def __init__(self,): 
		self.name = "UNSOCIABLE"
		self.definitions = [u'not liking to meet people or to spend time with them']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
