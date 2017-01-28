

#calss header
class _YIELDING():
	def __init__(self,): 
		self.name = "YIELDING"
		self.definitions = [u'Soft substances or qualities that are yielding can bend: ', u'A yielding person can change the way they normally behave or deal with situations when it is helpful or necessary.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
