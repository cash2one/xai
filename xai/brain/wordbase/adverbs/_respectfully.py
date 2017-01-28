

#calss header
class _RESPECTFULLY():
	def __init__(self,): 
		self.name = "RESPECTFULLY"
		self.definitions = [u'in a way that shows you want to be polite or honour someone: ', u'in a way that shows you admire someone or something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
