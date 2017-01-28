

#calss header
class _INFLAMMATORY():
	def __init__(self,): 
		self.name = "INFLAMMATORY"
		self.definitions = [u'intended or likely to cause anger or hate: ', u'causing or related to swelling and pain in the body']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
