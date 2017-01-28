

#calss header
class _LATER():
	def __init__(self,): 
		self.name = "LATER"
		self.definitions = [u'at a time in the future or after the time you have mentioned: ', u'at a time in the future, or after the time you have mentioned: ', u'not after: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
