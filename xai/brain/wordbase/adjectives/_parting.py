

#calss header
class _PARTING():
	def __init__(self,): 
		self.name = "PARTING"
		self.definitions = [u'done while leaving or separating: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
