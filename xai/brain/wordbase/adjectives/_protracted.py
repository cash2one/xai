

#calss header
class _PROTRACTED():
	def __init__(self,): 
		self.name = "PROTRACTED"
		self.definitions = [u'lasting for a long time or made to last longer than necessary: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
