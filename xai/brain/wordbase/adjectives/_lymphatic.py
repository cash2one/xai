

#calss header
class _LYMPHATIC():
	def __init__(self,): 
		self.name = "LYMPHATIC"
		self.definitions = [u'relating to lymph (= a liquid that transports useful substances around the body and carries waste matter away from body tissue): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
