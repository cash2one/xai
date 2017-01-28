

#calss header
class _INACCURATE():
	def __init__(self,): 
		self.name = "INACCURATE"
		self.definitions = [u'not completely correct or exact, or not able to do something correctly or exactly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
