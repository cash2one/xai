

#calss header
class _NAUSEATINGLY():
	def __init__(self,): 
		self.name = "NAUSEATINGLY"
		self.definitions = [u'in a way that makes you feel as if you want to vomit', u'in a way that you dislike and disapprove of: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
