

#calss header
class _COVETOUS():
	def __init__(self,): 
		self.name = "COVETOUS"
		self.definitions = [u'wanting to have something too much, especially something that belongs to someone else: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
