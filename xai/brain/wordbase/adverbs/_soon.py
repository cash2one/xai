

#calss header
class _SOON():
	def __init__(self,): 
		self.name = "SOON"
		self.definitions = [u'in or within a short time; before long; quickly: ', u'at the same time or a very short time after: ', u'If you do something as soon as possible, you do it as quickly as you can: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
