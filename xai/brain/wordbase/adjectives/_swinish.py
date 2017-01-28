

#calss header
class _SWINISH():
	def __init__(self,): 
		self.name = "SWINISH"
		self.definitions = [u'like a pig: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
