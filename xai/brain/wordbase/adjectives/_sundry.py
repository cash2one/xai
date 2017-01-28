

#calss header
class _SUNDRY():
	def __init__(self,): 
		self.name = "SUNDRY"
		self.definitions = [u'several different; various: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
