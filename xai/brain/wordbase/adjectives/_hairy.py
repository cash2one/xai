

#calss header
class _HAIRY():
	def __init__(self,): 
		self.name = "HAIRY"
		self.definitions = [u'having a lot of hair, especially on parts of the body other than the head: ', u'frightening or dangerous, especially in a way that is exciting: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
