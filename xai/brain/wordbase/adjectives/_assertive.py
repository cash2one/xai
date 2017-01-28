

#calss header
class _ASSERTIVE():
	def __init__(self,): 
		self.name = "ASSERTIVE"
		self.definitions = [u'Someone who is assertive behaves confidently and is not frightened to say what they want or believe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
