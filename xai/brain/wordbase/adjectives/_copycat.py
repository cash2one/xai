

#calss header
class _COPYCAT():
	def __init__(self,): 
		self.name = "COPYCAT"
		self.definitions = [u'done or made to be very similar to something else: ', u'A copycat crime is believed to have been influenced by another, often famous, crime because it is so similar: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
