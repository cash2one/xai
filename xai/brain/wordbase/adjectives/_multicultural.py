

#calss header
class _MULTICULTURAL():
	def __init__(self,): 
		self.name = "MULTICULTURAL"
		self.definitions = [u'including people who have many different customs and beliefs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
