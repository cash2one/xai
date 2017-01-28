

#calss header
class _PRODUCTIVE():
	def __init__(self,): 
		self.name = "PRODUCTIVE"
		self.definitions = [u'resulting in or providing a large amount or supply of something: ', u'having positive results: ', u'relating to the ability to produce language, rather than just understand it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
