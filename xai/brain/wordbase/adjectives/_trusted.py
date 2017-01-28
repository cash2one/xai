

#calss header
class _TRUSTED():
	def __init__(self,): 
		self.name = "TRUSTED"
		self.definitions = [u'deserving of trust, or able to be depended on : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
