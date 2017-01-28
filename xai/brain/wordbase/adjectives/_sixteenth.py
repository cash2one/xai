

#calss header
class _SIXTEENTH():
	def __init__(self,): 
		self.name = "SIXTEENTH"
		self.definitions = [u'16th written as a word: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
