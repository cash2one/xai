

#calss header
class _FOAMY():
	def __init__(self,): 
		self.name = "FOAMY"
		self.definitions = [u'made of or producing a mass of very small bubbles: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
