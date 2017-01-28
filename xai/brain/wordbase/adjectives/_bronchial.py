

#calss header
class _BRONCHIAL():
	def __init__(self,): 
		self.name = "BRONCHIAL"
		self.definitions = [u'of the pipes that carry air from the windpipe (= tube in the throat) to the lungs: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
