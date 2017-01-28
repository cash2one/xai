

#calss header
class _HOLOCENE():
	def __init__(self,): 
		self.name = "HOLOCENE"
		self.definitions = [u'from or referring to the period of time beginning at the end of the Pleistocene (= around 11,000 years ago) and continuing to the present: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
