

#calss header
class _HEREUPON():
	def __init__(self,): 
		self.name = "HEREUPON"
		self.definitions = [u'at this point in time']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
