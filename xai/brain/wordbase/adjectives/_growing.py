

#calss header
class _GROWING():
	def __init__(self,): 
		self.name = "GROWING"
		self.definitions = [u'increasing in size or quantity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
