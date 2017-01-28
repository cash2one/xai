

#calss header
class _ADORABLE():
	def __init__(self,): 
		self.name = "ADORABLE"
		self.definitions = [u'used to describe people or animals that are easy to love because they are so attractive and often small: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
