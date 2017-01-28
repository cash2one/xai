

#calss header
class _FRUITY():
	def __init__(self,): 
		self.name = "FRUITY"
		self.definitions = [u'smelling or tasting of fruit: ', u'(of a remark) humorous in a slightly shocking way: ', u'(of a voice) deep and pleasant']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
