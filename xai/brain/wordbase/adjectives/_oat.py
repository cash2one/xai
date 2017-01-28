

#calss header
class _OAT():
	def __init__(self,): 
		self.name = "OAT"
		self.definitions = [u'made of or from oats: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
