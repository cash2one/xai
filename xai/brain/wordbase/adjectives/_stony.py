

#calss header
class _STONY():
	def __init__(self,): 
		self.name = "STONY"
		self.definitions = [u'Stony ground contains a lot of stones: ', u'A stony expression or way of behaving is one that shows no sympathy or kindness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
