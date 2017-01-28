

#calss header
class _HEREDITARY():
	def __init__(self,): 
		self.name = "HEREDITARY"
		self.definitions = [u'(of characteristics or diseases) passed from the genes of a parent to a child, or (of titles and positions in society) passed from parent to a child as a right: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
