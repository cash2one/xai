

#calss header
class _CONTENTIOUS():
	def __init__(self,): 
		self.name = "CONTENTIOUS"
		self.definitions = [u'causing or likely to cause disagreement: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
