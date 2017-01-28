

#calss header
class _RATTY():
	def __init__(self,): 
		self.name = "RATTY"
		self.definitions = [u'feeling annoyed: ', u'looking old and in bad condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
