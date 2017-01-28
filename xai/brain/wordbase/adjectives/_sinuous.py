

#calss header
class _SINUOUS():
	def __init__(self,): 
		self.name = "SINUOUS"
		self.definitions = [u'moving in a twisting, curving, or indirect way, or having many curves: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
