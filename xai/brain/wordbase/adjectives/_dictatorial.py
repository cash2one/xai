

#calss header
class _DICTATORIAL():
	def __init__(self,): 
		self.name = "DICTATORIAL"
		self.definitions = [u'liking to give orders: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
