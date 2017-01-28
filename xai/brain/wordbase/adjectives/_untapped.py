

#calss header
class _UNTAPPED():
	def __init__(self,): 
		self.name = "UNTAPPED"
		self.definitions = [u'If a supply of something valuable is untapped, it is not yet used or taken advantage of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
