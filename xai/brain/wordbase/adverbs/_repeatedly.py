

#calss header
class _REPEATEDLY():
	def __init__(self,): 
		self.name = "REPEATEDLY"
		self.definitions = [u'many times: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
