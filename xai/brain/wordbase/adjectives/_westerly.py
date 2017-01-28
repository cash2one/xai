

#calss header
class _WESTERLY():
	def __init__(self,): 
		self.name = "WESTERLY"
		self.definitions = [u'in or towards the west: ', u'a wind that comes from the west']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
