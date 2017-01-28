

#calss header
class _UNORIGINAL():
	def __init__(self,): 
		self.name = "UNORIGINAL"
		self.definitions = [u'the same as a lot of other things and therefore not interesting or special']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
