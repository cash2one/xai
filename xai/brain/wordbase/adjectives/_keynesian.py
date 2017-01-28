

#calss header
class _KEYNESIAN():
	def __init__(self,): 
		self.name = "KEYNESIAN"
		self.definitions = [u'relating to the economic principles of John Maynard Keynes, especially the importance of having government plans to create jobs and encourage spending: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
