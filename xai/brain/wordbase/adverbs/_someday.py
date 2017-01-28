

#calss header
class _SOMEDAY():
	def __init__(self,): 
		self.name = "SOMEDAY"
		self.definitions = [u'at some time in the future that is not yet known or not stated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
