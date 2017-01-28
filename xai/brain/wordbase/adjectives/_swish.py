

#calss header
class _SWISH():
	def __init__(self,): 
		self.name = "SWISH"
		self.definitions = [u'fashionable or expensive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
