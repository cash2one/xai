

#calss header
class _CHEERLESS():
	def __init__(self,): 
		self.name = "CHEERLESS"
		self.definitions = [u'not bright or pleasant and making you feel sad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
