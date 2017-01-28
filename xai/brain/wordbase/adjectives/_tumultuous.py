

#calss header
class _TUMULTUOUS():
	def __init__(self,): 
		self.name = "TUMULTUOUS"
		self.definitions = [u'very loud, or full of confusion, change, or uncertainty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
