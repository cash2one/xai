

#calss header
class _CORRECTIVE():
	def __init__(self,): 
		self.name = "CORRECTIVE"
		self.definitions = [u'intended to improve a situation: ', u'used to refer to something that is intended to cure a medical condition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
