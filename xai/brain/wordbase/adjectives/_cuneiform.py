

#calss header
class _CUNEIFORM():
	def __init__(self,): 
		self.name = "CUNEIFORM"
		self.definitions = [u'of a form of writing used for over 3,000 years until the 1st century BC in the ancient countries of Western Asia', u'pointed at one end and wide at the other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
