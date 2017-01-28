

#calss header
class _INTERSTATE():
	def __init__(self,): 
		self.name = "INTERSTATE"
		self.definitions = [u'involving two or more of the states into which some countries such as the US are divided: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
