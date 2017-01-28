

#calss header
class _MADCAP():
	def __init__(self,): 
		self.name = "MADCAP"
		self.definitions = [u'used to describe silly and funny behaviour or a plan that is very silly and funny and unlikely to succeed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
