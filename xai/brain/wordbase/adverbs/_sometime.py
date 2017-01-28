

#calss header
class _SOMETIME():
	def __init__(self,): 
		self.name = "SOMETIME"
		self.definitions = [u'at a time in the future or the past that is not known or not stated: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
