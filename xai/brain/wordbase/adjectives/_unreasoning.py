

#calss header
class _UNREASONING():
	def __init__(self,): 
		self.name = "UNREASONING"
		self.definitions = [u'Unreasoning feelings or beliefs are not based on reason or judgment: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
