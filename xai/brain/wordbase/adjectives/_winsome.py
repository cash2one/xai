

#calss header
class _WINSOME():
	def __init__(self,): 
		self.name = "WINSOME"
		self.definitions = [u'attractive and pleasing, with simple qualities, sometimes like those a child has: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
