

#calss header
class _PEEVISH():
	def __init__(self,): 
		self.name = "PEEVISH"
		self.definitions = [u'easily annoyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
