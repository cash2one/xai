

#calss header
class _PITIFUL():
	def __init__(self,): 
		self.name = "PITIFUL"
		self.definitions = [u'making people feel sympathy: ', u'used to say that you consider something to be very bad or not satisfactory or not enough: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
