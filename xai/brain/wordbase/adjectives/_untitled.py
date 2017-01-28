

#calss header
class _UNTITLED():
	def __init__(self,): 
		self.name = "UNTITLED"
		self.definitions = [u'An untitled work does not have a title: ', u'An untitled person does not have an official title: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
