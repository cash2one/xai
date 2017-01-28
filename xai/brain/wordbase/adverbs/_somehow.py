

#calss header
class _SOMEHOW():
	def __init__(self,): 
		self.name = "SOMEHOW"
		self.definitions = [u'in a way or by some means that is not known or not stated: ', u'for a reason that is not clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
