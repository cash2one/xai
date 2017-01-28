

#calss header
class _BEHIND():
	def __init__(self,): 
		self.name = "BEHIND"
		self.definitions = [u'in the place where someone or something was before: ', u'slower or later than someone else, or than you should be: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
