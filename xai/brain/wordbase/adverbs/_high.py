

#calss header
class _HIGH():
	def __init__(self,): 
		self.name = "HIGH"
		self.definitions = [u'at or to a large distance from the ground: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
