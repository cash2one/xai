

#calss header
class _OTHERWORLDLY():
	def __init__(self,): 
		self.name = "OTHERWORLDLY"
		self.definitions = [u'more closely connected to spiritual things than to the ordinary things of life: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
