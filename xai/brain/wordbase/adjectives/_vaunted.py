

#calss header
class _VAUNTED():
	def __init__(self,): 
		self.name = "VAUNTED"
		self.definitions = [u'praised often in a way that is considered to be more than acceptable or reasonable: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
