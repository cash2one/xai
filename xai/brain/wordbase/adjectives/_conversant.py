

#calss header
class _CONVERSANT():
	def __init__(self,): 
		self.name = "CONVERSANT"
		self.definitions = [u'to be familiar with, and have knowledge or experience of the facts or rules of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
