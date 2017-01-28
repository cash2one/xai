

#calss header
class _BLOATED():
	def __init__(self,): 
		self.name = "BLOATED"
		self.definitions = [u'swollen and rounded because of containing too much air, liquid, or food: ', u'larger or richer than necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
