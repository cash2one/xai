

#calss header
class _CLAUSTROPHOBIC():
	def __init__(self,): 
		self.name = "CLAUSTROPHOBIC"
		self.definitions = [u'A claustrophobic place is small and closed, and makes you feel uncomfortable when you are in it: ', u'used to refer to a person suffering from a fear of being in closed spaces']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
