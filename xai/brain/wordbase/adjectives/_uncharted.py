

#calss header
class _UNCHARTED():
	def __init__(self,): 
		self.name = "UNCHARTED"
		self.definitions = [u'An uncharted place or situation is completely new and therefore has never been described before: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
