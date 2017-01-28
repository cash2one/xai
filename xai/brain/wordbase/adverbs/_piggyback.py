

#calss header
class _PIGGYBACK():
	def __init__(self,): 
		self.name = "PIGGYBACK"
		self.definitions = [u"on someone's back, or on the back of something: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
