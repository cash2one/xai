

#calss header
class _MOMENTARY():
	def __init__(self,): 
		self.name = "MOMENTARY"
		self.definitions = [u'lasting for a very short time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
