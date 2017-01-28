

#calss header
class _HEADLINE():
	def __init__(self,): 
		self.name = "HEADLINE"
		self.definitions = [u'a headline amount, number, or rate is the most important one or the one that people notice most: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
