

#calss header
class _PURPOSEFUL():
	def __init__(self,): 
		self.name = "PURPOSEFUL"
		self.definitions = [u'showing that you know what you want to do: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
