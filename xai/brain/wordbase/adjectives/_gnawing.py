

#calss header
class _GNAWING():
	def __init__(self,): 
		self.name = "GNAWING"
		self.definitions = [u'continuously uncomfortable, worrying, or painful: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
