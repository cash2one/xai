

#calss header
class _TANGLED():
	def __init__(self,): 
		self.name = "TANGLED"
		self.definitions = [u'twisted into an untidy mass: ', u'confused and complicated: ', u'involved in something bad: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
