

#calss header
class _INEXACT():
	def __init__(self,): 
		self.name = "INEXACT"
		self.definitions = [u'not exact or not known in detail: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
