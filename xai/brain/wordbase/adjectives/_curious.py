

#calss header
class _CURIOUS():
	def __init__(self,): 
		self.name = "CURIOUS"
		self.definitions = [u'interested in learning about people or things around you: ', u'strange and unusual: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
