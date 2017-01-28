

#calss header
class _CERTIFIABLE():
	def __init__(self,): 
		self.name = "CERTIFIABLE"
		self.definitions = [u'mentally ill', u'behaving in a silly or stupid way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
