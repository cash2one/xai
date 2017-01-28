

#calss header
class _STRAINED():
	def __init__(self,): 
		self.name = "STRAINED"
		self.definitions = [u'If a relationship is strained, problems are spoiling it: ', u'showing that someone is nervous or worried: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
