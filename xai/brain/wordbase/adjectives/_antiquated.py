

#calss header
class _ANTIQUATED():
	def __init__(self,): 
		self.name = "ANTIQUATED"
		self.definitions = [u'old-fashioned or unsuitable for modern society: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
