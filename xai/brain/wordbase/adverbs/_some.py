

#calss header
class _SOME():
	def __init__(self,): 
		self.name = "SOME"
		self.definitions = [u'used before a number to mean approximately; about: ', u'by a small amount or degree; a little: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
