

#calss header
class _RIGHTLY():
	def __init__(self,): 
		self.name = "RIGHTLY"
		self.definitions = [u'behaving in a way that is suitable and acceptable: ', u'used to mean that something may or may not be morally correct, but it is a fact: ', u'in a correct or exact way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
