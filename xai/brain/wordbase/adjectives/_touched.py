

#calss header
class _TOUCHED():
	def __init__(self,): 
		self.name = "TOUCHED"
		self.definitions = [u'grateful for something kind that someone has done: ', u'behaving in an unusual and strange way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
