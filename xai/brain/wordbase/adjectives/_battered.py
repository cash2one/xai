

#calss header
class _BATTERED():
	def __init__(self,): 
		self.name = "BATTERED"
		self.definitions = [u'hurt by being repeatedly hit: ', u'damaged, especially by being used a lot: ', u'covered with a mixture of flour, eggs, and milk before being cooked: ', u'very drunk']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
