

#calss header
class _QUALITY():
	def __init__(self,): 
		self.name = "QUALITY"
		self.definitions = [u'of a high standard: ', u'very good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
