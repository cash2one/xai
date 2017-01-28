

#calss header
class _ASCENDING():
	def __init__(self,): 
		self.name = "ASCENDING"
		self.definitions = [u'increasing in size or value: ', u'moving upwards or to higher levels, often used to refer to sensory pathways in the nervous system']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
