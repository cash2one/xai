

#calss header
class _YET():
	def __init__(self,): 
		self.name = "YET"
		self.definitions = [u'(and) despite that; used to add something that seems surprising because of what you have just said: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
