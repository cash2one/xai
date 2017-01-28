

#calss header
class _LUMBAR():
	def __init__(self,): 
		self.name = "LUMBAR"
		self.definitions = [u'relating to the lower part of the back']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
