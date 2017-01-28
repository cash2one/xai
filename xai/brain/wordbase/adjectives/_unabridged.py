

#calss header
class _UNABRIDGED():
	def __init__(self,): 
		self.name = "UNABRIDGED"
		self.definitions = [u'An unabridged book, speech, or article is in its original form and has not been made shorter.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
