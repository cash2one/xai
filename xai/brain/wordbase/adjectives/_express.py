

#calss header
class _EXPRESS():
	def __init__(self,): 
		self.name = "EXPRESS"
		self.definitions = [u'moving or being sent fast: ', u'clearly and intentionally stated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
