

#calss header
class _CONDITIONAL():
	def __init__(self,): 
		self.name = "CONDITIONAL"
		self.definitions = [u'(relating to) a sentence, often starting with "if" or "unless", in which one half expresses something which depends on the other half: ', u'(a form of a verb) expressing the idea that one thing depends on another thing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
