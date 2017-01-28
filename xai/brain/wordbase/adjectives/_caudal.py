

#calss header
class _CAUDAL():
	def __init__(self,): 
		self.name = "CAUDAL"
		self.definitions = [u'relating to the bottom end of the body, that is the bottom of the feet, or to the bottom end of the spinal cord: ', u'relating to something that is like a tail']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
