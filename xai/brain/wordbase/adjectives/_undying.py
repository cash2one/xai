

#calss header
class _UNDYING():
	def __init__(self,): 
		self.name = "UNDYING"
		self.definitions = [u'Undying feelings or beliefs are permanent and never end: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
