

#calss header
class _HANDMADE():
	def __init__(self,): 
		self.name = "HANDMADE"
		self.definitions = [u'made using the hands rather than a machine: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
