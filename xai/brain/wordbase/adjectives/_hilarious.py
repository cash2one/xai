

#calss header
class _HILARIOUS():
	def __init__(self,): 
		self.name = "HILARIOUS"
		self.definitions = [u'extremely funny and causing a lot of laughter: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
