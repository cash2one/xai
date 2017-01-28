

#calss header
class _AGNOSTIC():
	def __init__(self,): 
		self.name = "AGNOSTIC"
		self.definitions = [u'having the beliefs of an agnostic', u'relating to hardware or software that can be used with many different types of platform (= system)']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
