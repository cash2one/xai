

#calss header
class _DISTINGUISHED():
	def __init__(self,): 
		self.name = "DISTINGUISHED"
		self.definitions = [u'used to describe a respected and admired person, or their work: ', u'used to describe a person, especially an older person, who looks formal, stylish, or wise: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
