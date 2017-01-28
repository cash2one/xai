

#calss header
class _ENLIGHTENED():
	def __init__(self,): 
		self.name = "ENLIGHTENED"
		self.definitions = [u'showing understanding, acting in a positive way, and not following old-fashioned or false beliefs: ', u'knowing the truth about existence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
