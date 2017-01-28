

#calss header
class _TITILLATING():
	def __init__(self,): 
		self.name = "TITILLATING"
		self.definitions = [u'used to describe sexual images or descriptions, etc. that intentionally cause excitement, but not in a serious way: ', u'interesting and shocking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
