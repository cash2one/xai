

#calss header
class _REDUNDANT():
	def __init__(self,): 
		self.name = "REDUNDANT"
		self.definitions = [u'(especially of a word, phrase, etc.) unnecessary because it is more than is needed: ', u'having lost your job because your employer no longer needs you: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
