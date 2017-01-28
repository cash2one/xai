

#calss header
class _FORMALLY():
	def __init__(self,): 
		self.name = "FORMALLY"
		self.definitions = [u'officially: ', u'in a serious and correct way: ', u'(of garden design) in a way that is carefully designed and kept according to a plan']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
