

#calss header
class _ROCOCO():
	def __init__(self,): 
		self.name = "ROCOCO"
		self.definitions = [u'relating to the very decorated and detailed style in buildings, art, and furniture that was popular in Europe in the 18th century']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
