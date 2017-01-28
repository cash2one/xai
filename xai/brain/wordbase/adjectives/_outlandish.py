

#calss header
class _OUTLANDISH():
	def __init__(self,): 
		self.name = "OUTLANDISH"
		self.definitions = [u'strange and unusual and difficult to accept or like: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
