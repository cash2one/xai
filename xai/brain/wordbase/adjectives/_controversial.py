

#calss header
class _CONTROVERSIAL():
	def __init__(self,): 
		self.name = "CONTROVERSIAL"
		self.definitions = [u'causing disagreement or discussion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
