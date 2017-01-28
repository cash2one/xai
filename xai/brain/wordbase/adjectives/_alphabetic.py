

#calss header
class _ALPHABETIC():
	def __init__(self,): 
		self.name = "ALPHABETIC"
		self.definitions = [u'An alphabetic language has a letter or combinations of letters and marks to represent each speech sound in the language.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
