

#calss header
class _FARTHEST():
	def __init__(self,): 
		self.name = "FARTHEST"
		self.definitions = [u'at the greatest distance from sth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
