

#calss header
class _LORN():
	def __init__(self,): 
		self.name = "LORN"
		self.definitions = [u'alone and unhappy; left alone and not cared for']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
