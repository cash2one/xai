

#calss header
class _THYROID():
	def __init__(self,): 
		self.name = "THYROID"
		self.definitions = [u'relating to the thyroid gland: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
