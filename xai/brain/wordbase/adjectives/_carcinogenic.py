

#calss header
class _CARCINOGENIC():
	def __init__(self,): 
		self.name = "CARCINOGENIC"
		self.definitions = [u'used to refer to a substance that causes cancer']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
