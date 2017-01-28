

#calss header
class _SERVING():
	def __init__(self,): 
		self.name = "SERVING"
		self.definitions = [u'employed at the present time in a particular organization, especially the armed forces: ', u'an object used for holding food before it is put onto plates, or for putting food onto plates']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
