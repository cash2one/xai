

#calss header
class _FEY():
	def __init__(self,): 
		self.name = "FEY"
		self.definitions = [u'mysterious and strange, or trying to appear like this: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
