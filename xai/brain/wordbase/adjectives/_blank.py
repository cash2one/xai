

#calss header
class _BLANK():
	def __init__(self,): 
		self.name = "BLANK"
		self.definitions = [u'empty or clear, or containing no information or mark: ', u'showing no understanding or no emotion in the expression on your face: ', u'complete and absolute: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
