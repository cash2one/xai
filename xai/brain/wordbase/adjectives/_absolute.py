

#calss header
class _ABSOLUTE():
	def __init__(self,): 
		self.name = "ABSOLUTE"
		self.definitions = [u'very great or to the largest degree possible: ', u'used when expressing a strong opinion: ', u'true, right, or the same in all situations and not depending on anything else: ', u'An absolute ruler has unlimited power: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
