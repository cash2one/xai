

#calss header
class _INTERROGATIVE():
	def __init__(self,): 
		self.name = "INTERROGATIVE"
		self.definitions = [u'in the form of a question, or used in questions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
