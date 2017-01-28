

#calss header
class _NAY():
	def __init__(self,): 
		self.name = "NAY"
		self.definitions = [u'used to introduce a second and more extreme phrase in a sentence when the first phrase was not strong enough: ', u'Northern for  no adverb : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
