

#calss header
class _FEARFULLY():
	def __init__(self,): 
		self.name = "FEARFULLY"
		self.definitions = [u'with fear: ', u'extremely: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
