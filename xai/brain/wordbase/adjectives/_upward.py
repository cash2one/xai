

#calss header
class _UPWARD():
	def __init__(self,): 
		self.name = "UPWARD"
		self.definitions = [u'moving towards a higher position, level, or value: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
