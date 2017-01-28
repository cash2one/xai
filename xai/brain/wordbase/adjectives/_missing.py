

#calss header
class _MISSING():
	def __init__(self,): 
		self.name = "MISSING"
		self.definitions = [u'Someone who is missing has disappeared: ', u'Something that is missing cannot be found because it is not where it should be: ', u'Missing soldiers or military vehicles have not returned from fighting in a war but are not known completely certainly to be dead or destroyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
