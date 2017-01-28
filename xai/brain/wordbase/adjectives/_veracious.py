

#calss header
class _VERACIOUS():
	def __init__(self,): 
		self.name = "VERACIOUS"
		self.definitions = [u'honest and not telling or containing any lies: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
